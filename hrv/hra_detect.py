from heartpy import heartpy
from pandas import read_csv


# df = read_csv(filepath_or_buffer='../SendData4/data.csv')
df = read_csv(filepath_or_buffer='../SendData4/sampleDataBM.csv')
fs = 500.0
raw_ecg = df[:7500]['ECG'].values.flatten()
filtered_ecg = heartpy.enhance_peaks(raw_ecg)
# raw_ecg = df.values.flatten()

"""
Test using heartpy library
"""
working_data, measures = heartpy.process(hrdata=filtered_ecg, sample_rate=fs)
heartpy.plotter(working_data=working_data, measures=measures)

