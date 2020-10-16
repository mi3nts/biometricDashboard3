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



print("looking for stream...")
streams = resolve_stream()
inlet = StreamInlet(streams[0])
print("Stream found")
amtData = 0
resp_processing = QRSDetectorOnline()
x = []
total_peaks = []
val = 0
#data, _ = hp.load_exampledata(0)
#wd, m = hp.process(data, 100.0)
while True:
    sample, timestamp = inlet.pull_sample()
#data = pd.read_csv(r'/Users/vihasgowreddy/Desktop/Biometrics_Respiration/sampleRespData/sampleRespData_walking.txt')
    ecg_signal = sample[68]
    rr_list = resp_processing.process_measurement(ecg_signal)
    amtData = amtData + 1
    if len(rr_list) > 5:
        m, wd = resp_processing.calc_breathing(rr_list)
        #val = m['breathingrate']
        if m['breathingrate'] != val:
            val = m['breathingrate']
            print(val)
        #print(rr_list)
    time.sleep(.1)
    if (amtData == 30000):
        break
        #print(resp_processing.calculate_hrv(rr_list))
    #amtData += 50
#columnsToPlot = pd.DataFrame(data, columns = ['Resp']).values.flatten()
#columnsToPlot = pd.DataFrame(data).values.flatten()
    
#FIND NORMALIZE FUNCTION
#avg = sum(columnsToPlot) / len(columnsToPlot)
#stdDev = statistics.stdev(columnsToPlot)

#columnsToPlot[:] = [(x - avg)/stdDev for x in columnsToPlot] #NORMALIZE

    #
#olumnsToPlotNew = scipy.fftpack.fft(columnsToPlot)

#peaks, _ = scipy.signal.find_peaks(columnsToPlot, distance=250, prominence=1)
#peaksFound = 0
#print(pd.DataFrame(data, columns= ['Resp']).index.astype(np.int))
#output_file("line.html")
#p = figure(plot_width = 2000, plot_height=400)
#p.line(pd.DataFrame(data, columns= ['Resp']).index.astype(np.int), columnsToPlot, line_width=2)
#p.line(pd.DataFrame(data).index.astype(np.int), columnsToPlot, line_width=2)
#p.line(f, pxx, line_width=2)
#p.line(columnsToPlot.index.astype(np.int), columnsToPlot, line_width=2)
#for x in peaks:
#    if x <= 150000:
#        peaksFound += 1
#    p.circle(x, columnsToPlot[x], size=5, color="red", alpha = 0.5)
#p.circle(2700, columnsToPlot[2700], size=5, color="red", alpha = 0.5) #GET RID OF
#.circle(12200, columnsToPlot[12200], size=5, color="red", alpha = 0.5)#GET RID OF
#p.circle(16150, columnsToPlot[16150], size=5, color="red", alpha = 0.5)#GET RID OF
#show(p)
#print(rr_list.len())
#print(peaks)
#print(f'Respiration Rate: {peaksFound/5}')



#TOTAL BREATHING RATE
# columnsToPlot = pd.DataFrame(data[:30000]).values.flatten()
# print(columnsToPlot)
# rr_list = []
# for val in columnsToPlot:
#     rr_list.append(resp_processing.process_measurement(val))
# print(rr_list)
# m, wd = resp_processing.calc_breathing(rr_list)
# print(m['breathingrate'])