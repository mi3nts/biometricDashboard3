# FUNCTION TO CREATE COLUMN DATA SOURCE BOKEH DATA STRUCTURE TO EFFICENTLY STORE
# AND UPDATE BM DATA

# CODE AUTHORED BY: SHAWHIN TALEBI
# THE UNIVERSITY OF TEXAS AT DALLAS
# MULTI-SCALE INTEGRATED REMOTE SENSING AND SIMULATION (MINTS)

from bokeh.models import ColumnDataSource

# define function
# inputs: none
# outputs: ColumnDataSource data structure for BM data
def mkColumnDataSources():
    dataDictionary = dict(eeg_1=[0], eeg_2=[0], eeg_3=[0], eeg_4=[0], \
    eeg_5=[0], eeg_6=[0], eeg_7=[0], eeg_8=[0], eeg_9=[0], eeg_10=[0],\
    eeg_11=[0], eeg_12=[0], eeg_13=[0], eeg_14=[0], eeg_15=[0], eeg_16=[0],\
    eeg_17=[0], eeg_18=[0], eeg_19=[0], eeg_20=[0], eeg_21=[0], eeg_22=[0],\
    eeg_23=[0], eeg_24=[0], eeg_25=[0], eeg_26=[0], eeg_27=[0], eeg_28=[0],\
    eeg_29=[0], eeg_30=[0], eeg_31=[0], eeg_32=[0], eeg_33=[0], eeg_34=[0],\
    eeg_35=[0], eeg_36=[0], eeg_37=[0], eeg_38=[0], eeg_39=[0], eeg_40=[0],\
    eeg_41=[0], eeg_42=[0], eeg_43=[0], eeg_44=[0], eeg_45=[0], eeg_46=[0],\
    eeg_47=[0], eeg_48=[0], eeg_49=[0], eeg_50=[0], eeg_51=[0], eeg_52=[0],\
    eeg_53=[0], eeg_54=[0], eeg_55=[0], eeg_56=[0], eeg_57=[0], eeg_58=[0],\
    eeg_59=[0], eeg_60=[0], eeg_61=[0], eeg_62=[0], eeg_63=[0], eeg_64=[0],\
    ecg_x=[0], ecg_y=[0])

    numDictionary = dict(num_x=[0], num_y=[0], \
    spo2=[str(0)], gsr=[str(0)], hrv=[str(0)], rr=[str(0)],\
    hr_x=[0], hr_y=[0], hr=[str(0)])

    # this must only be modified from a Bokeh session callback
    source = ColumnDataSource(data=dataDictionary)
    source_num = ColumnDataSource(data=numDictionary)

    return source, source_num