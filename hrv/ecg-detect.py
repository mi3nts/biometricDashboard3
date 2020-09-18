from ecgdetectors import Detectors
import numpy as np
import matplotlib.pyplot as plt


raw_data = np.loadtxt('sample.tsv')
raw_ecg = raw_data[:, 0]
fs = 250

detectors = Detectors(fs)
r_peaks = detectors.pan_tompkins_detector(unfiltered_ecg=raw_ecg)
nn_intervals = np.diff(r_peaks)
print(nn_intervals[1:])

plt.figure()
plt.plot(r_peaks, raw_ecg[r_peaks], 'ro')
plt.title('R Peaks')
plt.show()


