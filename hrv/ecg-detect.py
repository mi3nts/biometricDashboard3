from ecgdetectors import Detectors
import numpy as np
import matplotlib.pyplot as plt


raw_data = np.loadtxt('sample.tsv')
raw_ecg = raw_data[:, 0]
fs = 50

detectors = Detectors(fs)
r_peaks = detectors.pan_tompkins_detector(unfiltered_ecg=raw_ecg)
#r_peaks = detectors.hamilton_detector(unfiltered_ecg=raw_ecg)
print(r_peaks)
plt.figure()
plt.plot(raw_ecg)
plt.plot(r_peaks, raw_ecg[r_peaks], 'ro')
plt.title('R Peaks')
plt.show()


