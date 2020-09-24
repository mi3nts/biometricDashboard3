import heartpy
import ecgdetectors
from pandas import read_csv
import matplotlib.pyplot as plt

df = read_csv(filepath_or_buffer='../SendData4/sampleDataBM.csv')
raw_ecg = df[0:2000]["ECG"]
fs = 500

"""
Test using py-ecg-detectors library
"""
detector = ecgdetectors.Detectors(fs)
r_peaks = detector.pan_tompkins_detector(unfiltered_ecg=raw_ecg)
plt.figure()
plt.plot(raw_ecg)
plt.plot(r_peaks, raw_ecg[r_peaks], 'ro')
plt.title('py-ecg-detectors library R Peak results')
plt.show()


"""
Test using heartpy library
"""
working_data, measures = heartpy.process(raw_ecg, 500.0)
heartpy.plotter(working_data=working_data, measures=measures)

