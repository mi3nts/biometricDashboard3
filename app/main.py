# MAIN FILE FOR BM VISUALIZATION APPLICATION
# run via: bokeh serve --show .

# CODE AUTHORED BY: SHAWHIN TALEBI
# THE UNIVERSITY OF TEXAS AT DALLAS
# MULTI-SCALE INTEGRATED REMOTE SENSING AND SIMULATION (MINTS)

# import functions
from getStream import getStream
from mkColumnDataSource import mkColumnDataSource

# import visualization modules
from modules.eegModule import eegModule
from modules.ecgModule import ecgModule
from modules.spo2Module import spo2Module
from modules.gsrModule import gsrModule

# import bokeh modules
from bokeh.plotting import curdoc, figure
from bokeh.models import Text, Plot
from bokeh.layouts import column, row

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

# CREATE BOKEH DATA STRUCTURE TO EFFICENTLY STORE AND UPDATE DATA
# ------------------------------------------------------------------------------
source = mkColumnDataSource()

# DEFINE DOCUMENT OBJECT
# ------------------------------------------------------------------------------
# This is important! Save curdoc() to make sure all threads see the same
# document.
doc = curdoc()

i=0 # initialize x index

# DEFINE FUNCTIONS TO GET REAL TIME DATA
# ------------------------------------------------------------------------------
@gen.coroutine
def update(eeg_1, eeg_2, eeg_3, eeg_4, eeg_5, eeg_6, eeg_7, eeg_8, eeg_9, eeg_10,\
eeg_11, eeg_12, eeg_13, eeg_14, eeg_15, eeg_16,eeg_17, eeg_18, eeg_19, eeg_20, \
eeg_21, eeg_22, eeg_23, eeg_24, eeg_25, eeg_26, eeg_27, eeg_28, eeg_29, eeg_30, \
eeg_31, eeg_32, eeg_33, eeg_34, eeg_35, eeg_36, eeg_37, eeg_38, eeg_39, eeg_40,\
eeg_41, eeg_42, eeg_43, eeg_44, eeg_45, eeg_46, eeg_47, eeg_48, eeg_49, eeg_50, \
eeg_51, eeg_52, eeg_53, eeg_54, eeg_55, eeg_56, eeg_57, eeg_58, eeg_59, eeg_60, \
eeg_61, eeg_62, eeg_63, eeg_64,\
ecg_x, ecg_y, spo2, gsr):

    source.stream(dict(eeg_1=[eeg_1], eeg_2=[eeg_2], \
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
    eeg_63=[eeg_63], eeg_64=[eeg_64], \
    ecg_x=[ecg_x], ecg_y=[ecg_y], \
    spo2=[spo2], gsr=[gsr]), rollover=1500)

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
        eeg_59, eeg_60, eeg_61, eeg_62, eeg_63, eeg_64 = np.zeros([64,1])

        # append ecg data
        ecg_x, ecg_y = i, sample[68]

        # append spo2 data
        spo2 = 0;

        # append gsr data
        gsr = 0;

        # but update the document from callback
        doc.add_next_tick_callback(partial(update, eeg_1=eeg_1, eeg_2=eeg_2, \
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
        eeg_63=eeg_63, eeg_64=eeg_64, \
        ecg_x=ecg_x, ecg_y=ecg_y, \
        spo2=spo2, gsr=gsr))


# DEFINE VISUALIZATION MODULES
# ------------------------------------------------------------------------------
eeg = eegModule()
ecg = ecgModule(source)
spo2 = spo2Module()
gsr = gsrModule()

# CREATE LAYOUT
# ------------------------------------------------------------------------------
p = column(row(eeg.DeltaFig, eeg.ThetaFig, eeg.AlphaFig, eeg.TotalFig), \
           row(ecg.Fig, column(spo2.Fig, gsr.Fig)))


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
