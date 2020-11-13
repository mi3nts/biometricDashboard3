from bokeh.plotting import figure, output_file, show
import pandas as pd
import numpy as np
import scipy.signal
from collections import deque
import scipy.fftpack
import statistics
from pylsl import StreamInlet, resolve_stream
from QRSDetector import QRSDetectorOnline
import time
import heartpy as hp
import itertools
import datetime


def rr_changes(rr_list, rr_list_size, queue_limit, peaks_time, counter, num_rr_skipped, queue_end, listChanged):
    if (rr_list_size < queue_limit) and (len(rr_list) > rr_list_size):
        #print("List Changed")
        rr_list_size = rr_list_size + 1
        peaks_time.append(counter)
        listChanged = True
        if rr_list_size == queue_limit:
            queue_end = rr_list[-1]
    elif len(rr_list) == queue_limit and rr_list[-1] != queue_end: #Account for deque size being reached
        listChanged = True
        peaks_time.append(counter)
        num_rr_skipped = num_rr_skipped - 1
    
    return rr_list_size, listChanged, queue_end, num_rr_skipped


def find_resp(rr_list, counter, sampling_frequency, listChanged, peaks_time, num_rr_skipped):
    if len(rr_list) < 4:
        if counter == 1:
            return 0, num_rr_skipped
    elif len(rr_list) >= 4 and counter < (sampling_frequency * 8):
        temp = list(rr_list)
        if listChanged:
            m, wd = resp_processing.calc_breathing(temp, sampling_freq=sampling_frequency)
            val = m['breathingrate']
            return val, num_rr_skipped

    elif counter >= (sampling_frequency * 8):
        if (peaks_time[-1] - peaks_time[0]) > (sampling_frequency * 8):
            num_rr_skipped = num_rr_skipped + 1
            peaks_time.pop(0)
            listChanged = True

        temp = list(rr_list)
        temp = temp[num_rr_skipped:]

        if listChanged:
            m, wd = resp_processing.calc_breathing(temp, sampling_freq=sampling_frequency)
            val = m['breathingrate']
            return val, num_rr_skipped
    return -1, num_rr_skipped

print("looking for stream...")
streams = resolve_stream()
inlet = StreamInlet(streams[0])
print("Stream found")
resp_processing = QRSDetectorOnline()

rr_list_size = 0
counter = 0
peaks_time = list()
num_rr_skipped = 0
sampling_frequency = 500 #CHANGE WHEN NECESSARY
queue_limit = sampling_frequency * .8
queue_end = 0.0

while True:
    sample, timestamp = inlet.pull_sample()
    
    ecg_signal = sample[68]
    #row_signal = sample[82]

    listChanged = False

    #if counter == 0:
    #     print(f"Row Signal: {row_signal}")
         
    rr_list = resp_processing.process_measurement(ecg_signal)
    rr_list_size, listChanged, queue_end, num_rr_skipped = rr_changes(rr_list, rr_list_size, queue_limit, peaks_time, counter, num_rr_skipped, queue_end, listChanged)
    
    counter = counter + 1

    val, num_rr_skipped = find_resp(rr_list, counter, sampling_frequency, listChanged, peaks_time, num_rr_skipped)
    if val == -1:
        continue
    print(val)