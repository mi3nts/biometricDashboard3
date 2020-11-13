# MAIN FILE FOR BM VISUALIZATION APPLICATION
# run via: bokeh serve --show .

# CODE AUTHORED BY: SHAWHIN TALEBI
# THE UNIVERSITY OF TEXAS AT DALLAS
# MULTI-SCALE INTEGRATED REMOTE SENSING AND SIMULATION (MINTS)

# import functions
from functions.getStream import getStream
from functions.mkColumnDataSources import mkColumnDataSources
from functions.QRSDetectorOnline import QRSDetectorOnline

# import visualization modules
from modules.eegModule import eegModule
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

# RESOLVE INLET
# ------------------------------------------------------------------------------
# get data stream
inlet = getStream(0)

# initialize QRS detector
ecg_processing = QRSDetectorOnline()

# CREATE BOKEH DATA STRUCTURES TO EFFICENTLY STORE AND UPDATE DATA
# ------------------------------------------------------------------------------
source_eeg, source_ecg, source_num = mkColumnDataSources()

# DEFINE DOCUMENT OBJECT
# ------------------------------------------------------------------------------
# This is important! Save curdoc() to make sure all threads see the same
# document.
doc = curdoc()

i=0 # initialize x index (current sample number)

# DEFINE FUNCTIONS TO GET REAL TIME DATA
# ------------------------------------------------------------------------------
@gen.coroutine
def update_eeg(eeg_1, eeg_2, eeg_3, eeg_4, eeg_5, eeg_6, eeg_7, eeg_8, eeg_9, eeg_10,\
eeg_11, eeg_12, eeg_13, eeg_14, eeg_15, eeg_16,eeg_17, eeg_18, eeg_19, eeg_20, \
eeg_21, eeg_22, eeg_23, eeg_24, eeg_25, eeg_26, eeg_27, eeg_28, eeg_29, eeg_30, \
eeg_31, eeg_32, eeg_33, eeg_34, eeg_35, eeg_36, eeg_37, eeg_38, eeg_39, eeg_40,\
eeg_41, eeg_42, eeg_43, eeg_44, eeg_45, eeg_46, eeg_47, eeg_48, eeg_49, eeg_50, \
eeg_51, eeg_52, eeg_53, eeg_54, eeg_55, eeg_56, eeg_57, eeg_58, eeg_59, eeg_60, \
eeg_61, eeg_62, eeg_63, eeg_64):

    source_eeg.stream(dict(eeg_1=[eeg_1], eeg_2=[eeg_2], \
    eeg_3=[eeg_3], eeg_4=[eeg_4], eeg_5=[eeg_5], eeg_6=[eeg_6], eeg_7=[eeg_7], \
    eeg_8=[eeg_8], eeg_9=[eeg_9], eeg_10=[eeg_10],eeg_11=[eeg_11], eeg_12=[eeg_12], \
    eeg_13=[eeg_13], eeg_14=[eeg_14], eeg_15=[eeg_15], eeg_16=[eeg_16], eeg_17=[eeg_17], \
    eeg_18=[eeg_18], eeg_19=[eeg_19], eeg_20=[eeg_20], eeg_21=[eeg_21], eeg_22=[eeg_22],\
    eeg_23=[eeg_23], eeg_24=[eeg_24], eeg_25=[eeg_25], eeg_26=[eeg_26], eeg_27=[eeg_27], \
    eeg_28=[eeg_28],eeg_29=[eeg_29], eeg_30=[eeg_30], eeg_31=[eeg_31], eeg_32=[eeg_32], \
    eeg_33=[eeg_33], eeg_34=[eeg_34],eeg_35=[eeg_35], eeg_36=[eeg_36], eeg_37=[eeg_37], \
    eeg_38=[eeg_38], eeg_39=[eeg_39], eeg_40=[eeg_40],eeg_41=[eeg_41], eeg_42=[eeg_42], \
    eeg_43=[eeg_43], eeg_44=[eeg_44], eeg_45=[eeg_45], eeg_46=[eeg_46],eeg_47=[eeg_47], \
    eeg_48=[eeg_48], eeg_49=[eeg_49], eeg_50=[eeg_50], eeg_51=[eeg_51], eeg_52=[eeg_52],\
    eeg_53=[eeg_53], eeg_54=[eeg_54], eeg_55=[eeg_55], eeg_56=[eeg_56], eeg_57=[eeg_57], \
    eeg_58=[eeg_58], eeg_59=[eeg_59], eeg_60=[eeg_60], eeg_61=[eeg_61], eeg_62=[eeg_62], \
    eeg_63=[eeg_63], eeg_64=[eeg_64]), rollover=1)

    eeg.visualize(i, source_eeg)

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
        global i
        # do some blocking computation

        # pause for 0.01 seconds
        time.sleep(0.01)
        # update x index
        i = i+1

        # get data from inlet
        sample, timestamp = inlet.pull_sample()

        # append eeg data
        eeg_1, eeg_2, eeg_3, eeg_4, \
        eeg_5, eeg_6, eeg_7, eeg_8, eeg_9, eeg_10,\
        eeg_11, eeg_12, eeg_13, eeg_14, eeg_15, eeg_16,\
        eeg_17, eeg_18, eeg_19, eeg_20, eeg_21, eeg_22,\
        eeg_23, eeg_24, eeg_25, eeg_26, eeg_27, eeg_28,\
        eeg_29, eeg_30, eeg_31, eeg_32, eeg_33, eeg_34,\
        eeg_35, eeg_36, eeg_37, eeg_38, eeg_39, eeg_40,\
        eeg_41, eeg_42, eeg_43, eeg_44, eeg_45, eeg_46,\
        eeg_47, eeg_48, eeg_49, eeg_50, eeg_51, eeg_52,\
        eeg_53, eeg_54, eeg_55, eeg_56, eeg_57, eeg_58,\
        eeg_59, eeg_60, eeg_61, eeg_62, eeg_63, eeg_64 = sample[:64]

        # append ecg data
        ecg_x, ecg_y = i, -sample[68]+6000

        # define position and value for hr
        hr_x, hr_y = i-24, 3800
        if i<25:
            hr_x=1
        # define text for hr display
        hr = 'HR=' + str(round(sample[72]))

        # compute currnt hrv
        measurements = ecg_processing.process_measurement(ecg_y)
        # if hrv is nan set it as 0
        if np.isnan(measurements['rmssd']):
            measurements['rmssd'] = 0

        # update number box visualizations
        num_x=1
        num_y=1

        spo2 = str(round(sample[71]))
        gsr = str(round(sample[73]))
        hrv = str(round(measurements['rmssd']))
        rr = str(round(sample[69]))

        # but update the document from callback
        doc.add_next_tick_callback(partial(update_eeg, eeg_1=eeg_1, eeg_2=eeg_2, \
        eeg_3=eeg_3, eeg_4=eeg_4, eeg_5=eeg_5, eeg_6=eeg_6, eeg_7=eeg_7, \
        eeg_8=eeg_8, eeg_9=eeg_9, eeg_10=eeg_10,eeg_11=eeg_11, eeg_12=eeg_12, \
        eeg_13=eeg_13, eeg_14=eeg_14, eeg_15=eeg_15, eeg_16=eeg_16, eeg_17=eeg_17, \
        eeg_18=eeg_18, eeg_19=eeg_19, eeg_20=eeg_20, eeg_21=eeg_21, eeg_22=eeg_22,\
        eeg_23=eeg_23, eeg_24=eeg_24, eeg_25=eeg_25, eeg_26=eeg_26, eeg_27=eeg_27, \
        eeg_28=eeg_28,eeg_29=eeg_29, eeg_30=eeg_30, eeg_31=eeg_31, eeg_32=eeg_32, \
        eeg_33=eeg_33, eeg_34=eeg_34,eeg_35=eeg_35, eeg_36=eeg_36, eeg_37=eeg_37, \
        eeg_38=eeg_38, eeg_39=eeg_39, eeg_40=eeg_40,eeg_41=eeg_41, eeg_42=eeg_42, \
        eeg_43=eeg_43, eeg_44=eeg_44, eeg_45=eeg_45, eeg_46=eeg_46,eeg_47=eeg_47, \
        eeg_48=eeg_48, eeg_49=eeg_49, eeg_50=eeg_50, eeg_51=eeg_51, eeg_52=eeg_52,\
        eeg_53=eeg_53, eeg_54=eeg_54, eeg_55=eeg_55, eeg_56=eeg_56, eeg_57=eeg_57, \
        eeg_58=eeg_58, eeg_59=eeg_59, eeg_60=eeg_60, eeg_61=eeg_61, eeg_62=eeg_62, \
        eeg_63=eeg_63, eeg_64=eeg_64))

        # update ecg
        doc.add_next_tick_callback(partial(update_ecg, ecg_x=ecg_x, ecg_y=ecg_y))

        # update numbers
        doc.add_next_tick_callback(partial(update_num, num_x=num_x, num_y=num_y, \
        spo2=spo2, gsr=gsr, hrv=hrv, rr=rr, hr_x=hr_x, hr_y=hr_y, hr=hr))


# DEFINE VISUALIZATION MODULES
# ------------------------------------------------------------------------------
eeg = eegModule()
ecg = ecgModule(source_ecg, source_num)
spo2 = spo2Module(source_num)
gsr = gsrModule(source_num)
hrv = hrvModule(source_num)
resp = respModule(source_num)

# CREATE LAYOUT
# ------------------------------------------------------------------------------
p = column(row(Spacer(width=300),eeg.AlphaFig, Spacer(width=200), eeg.TotalFig, Spacer(width=300)), \
           row(ecg.Fig, Spacer(width=125), column(hrv.Fig, resp.Fig, spo2.Fig, gsr.Fig)))

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
