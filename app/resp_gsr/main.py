# MAIN FILE FOR BM VISUALIZATION APPLICATION
# run via: bokeh serve --show .

# CODE AUTHORED BY: SHAWHIN TALEBI
# THE UNIVERSITY OF TEXAS AT DALLAS
# MULTI-SCALE INTEGRATED REMOTE SENSING AND SIMULATION (MINTS)

# import functions
from functions.getStream import getStream
from functions.mkColumnDataSources import mkColumnDataSources
from functions.QRSDetectorOnline import QRSDetectorOnline
from functions.rrHelpers import rr_changes, find_resp

# import visualization modules
from modules.ecgModule import ecgModule
from modules.spo2Module import spo2Module
from modules.gsrModule import gsrModule
from modules.hrvModule import hrvModule
from modules.respModule import respModule

# import bokeh modules
from bokeh.plotting import curdoc, figure
from bokeh.models import Text, Plot
from bokeh.layouts import column, row, Spacer

# # import other modules
from functools import partial
from tornado import gen
from threading import Thread
import time
import numpy as np
import sys

# RESOLVE INLET
# ------------------------------------------------------------------------------
# get data stream
inlet = getStream(0)

# INITIALIZER VARIABLES FOR HRV AND RR
# initialize QRS detector
ecg_processing = QRSDetectorOnline()

# initialize RR variables
rr_list_size = 0
peaks_time = list()
num_rr_skipped = 0
sampling_frequency = 500 #CHANGE WHEN NECESSARY
queue_limit = sampling_frequency * .8
queue_end = 0.0
last_val = 0.0

# CREATE BOKEH DATA STRUCTURES TO EFFICENTLY STORE AND UPDATE DATA
# ------------------------------------------------------------------------------
# source_eeg, source_ecg, source_num = mkColumnDataSources()
source_eeg, source_ecg, source_num= mkColumnDataSources()

# DEFINE DOCUMENT OBJECT
# ------------------------------------------------------------------------------
# This is important! Save curdoc() to make sure all threads see the same
# document.
doc = curdoc()

i=0 # initialize x index (current sample number)

# DEFINE FUNCTIONS TO GET REAL TIME DATA
# ------------------------------------------------------------------------------
@gen.coroutine
def update_ecg(ecg_x, ecg_y):

    source_ecg.stream(dict(ecg_x=[ecg_x], ecg_y=[ecg_y]), rollover=750)

@gen.coroutine
def update_num(num_x, num_y, spo2, gsr, hrv, rr, hr_x, hr_y, hr):

    source_num.stream(dict(num_x=[num_x], num_y=[num_y], \
    spo2=[spo2], gsr=[gsr], hrv=[hrv], rr=[rr], \
    hr_x=[hr_x], hr_y=[hr_y], hr=[hr]), rollover=1)


def blocking_task():
    while True:
        global i, rr_list_size, peaks_time, num_rr_skipped, sampling_frequency,\
        queue_limit, queue_end, last_val

        # do some blocking computation

        # pause for 0.01 seconds
        # update x index
        i = i+1
        # intialize listChanged variable
        list_changed = False

        # get data from inlet
        sample, timestamp = inlet.pull_sample()

        # append ecg data
        ecg_x, ecg_y = i, -sample[68]+6000

        # define position and value for hr
        hr_x, hr_y = i-24, 3800
        if i<25:
            hr_x=1
        # define text for hr display
        hr = 'HR=' + str(round(sample[72]))

        # compute currnt hrv
        measurements, rr_list = ecg_processing.process_measurement(ecg_y)

        # compute rr
        rr_list_size, list_changed, queue_end, num_rr_skipped = \
            rr_changes(rr_list, rr_list_size, queue_limit, peaks_time, i, num_rr_skipped, queue_end, list_changed)
        val, num_rr_skipped = find_resp(ecg_processing, rr_list, i, sampling_frequency, list_changed, peaks_time, num_rr_skipped)
        if val == -1:
            val = last_val

        # if hrv is nan set it as 0
        if np.isnan(measurements['rmssd']):
            measurements['rmssd'] = 0

        # update number box visualizations
        num_x=1
        num_y=1

        spo2 = str(round(sample[71]))
        gsr = str(round(sample[73]))
        hrv = str(round(measurements['rmssd']))
        rr = str(round(val, 3))


        last_val = val

        # update ecg
        doc.add_next_tick_callback(partial(update_ecg, ecg_x=ecg_x, ecg_y=ecg_y))

        # update numbers
        doc.add_next_tick_callback(partial(update_num, num_x=num_x, num_y=num_y, \
        spo2=spo2, gsr=gsr, hrv=hrv, rr=rr, hr_x=hr_x, hr_y=hr_y, hr=hr))


# DEFINE VISUALIZATION MODULES
# ------------------------------------------------------------------------------
ecg = ecgModule(source_ecg, source_num)
spo2 = spo2Module(source_num)
gsr = gsrModule(source_num)
hrv = hrvModule(source_num)
resp = respModule(source_num)

# CREATE LAYOUT
# ------------------------------------------------------------------------------
p = column(row(ecg.Fig, Spacer(width=125), column(hrv.Fig, resp.Fig, spo2.Fig, gsr.Fig)))

# MAKE PLOT THE ROOT OF DOCUMENT
# ------------------------------------------------------------------------------
doc.add_root(p)

# CREATE PARALLEL THREAD
# more info here: https://docs.python.org/2/library/threading.html#thread-objects
# ------------------------------------------------------------------------------
# create thread that calls the target
thread = Thread(target=blocking_task)
# start thread
thread.start()
