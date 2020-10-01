from ecgdetectors import Detectors
import numpy as np
import matplotlib.pyplot as plt


raw_data = np.loadtxt('../SendData4/data.csv')
# raw_ecg = raw_data[:, 0]
fs = 50

detectors = Detectors(fs)
r_peaks = detectors.pan_tompkins_detector(unfiltered_ecg=raw_data)
# r_peaks = detectors.hamilton_detector(unfiltered_ecg=raw_data)
print(r_peaks)
plt.figure()
plt.plot(raw_data)
plt.plot(r_peaks, raw_data[r_peaks], 'ro')
plt.title('R Peaks')
plt.show()


