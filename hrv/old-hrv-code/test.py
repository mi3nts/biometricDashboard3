"""
ONLY USE THIS FILE TO TEST DATA OFFLINE USING HEARTPY.
"""

from heartpy import heartpy
from pandas import read_csv
import matplotlib.pyplot as plt

# df = read_csv(filepath_or_buffer='../SendData4/data.csv')
df = read_csv(filepath_or_buffer='../SendData4/sampleDataBM.csv')
print(len(df))
fs = 500
raw_ecg = df[:2000]['ECG'].values.flatten()
filtered_ecg = heartpy.remove_baseline_wander(raw_ecg, fs)
filtered_ecg = heartpy.enhance_peaks(filtered_ecg)
# raw_ecg = df.values.flatten()

working_data, measures = heartpy.process(hrdata=filtered_ecg, sample_rate=fs)
r_peak_indexes = working_data['peaklist']
plt.figure()
plt.plot(raw_ecg)
plt.plot(r_peak_indexes, raw_ecg[r_peak_indexes], 'ro')
plt.title('BPI: {}'.format(measures['bpm']))
plt.show()
