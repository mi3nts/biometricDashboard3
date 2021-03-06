import numpy as np
from collections import deque
from scipy.signal import butter, lfilter, welch
from scipy.interpolate import UnivariateSpline


class QRSDetectorOnline(object):
    """
    Python Online ECG QRS Detector based on the Pan-Tomkins algorithm.
    Michał Sznajder (Jagiellonian University) - technical contact (msznajder@gmail.com)
    Marta Łukowska (Jagiellonian University)
    The module is online Python implementation of QRS complex detection in the ECG signal based
    on the Pan-Tomkins algorithm: Pan J, Tompkins W.J., A real-time QRS detection algorithm,
    IEEE Transactions on Biomedical Engineering, Vol. BME-32, No. 3, March 1985, pp. 230-236.
    The QRS complex corresponds to the depolarization of the right and left ventricles of the human heart. It is the most visually obvious part of the ECG signal. QRS complex detection is essential for time-domain ECG signal analyses, namely heart rate variability. It makes it possible to compute inter-beat interval (RR interval) values that correspond to the time between two consecutive R peaks. Thus, a QRS complex detector is an ECG-based heart contraction detector.
    Online version detects QRS complexes in a real-time acquired ECG signal. Therefore, it requires an ECG device to be plugged in and receiving a signal in real-time.
    This implementation of a QRS Complex Detector is by no means a certified medical tool and should not be used in health monitoring. It was created and used for experimental purposes in psychophysiology and psychology.
    You can find more information in module documentation:
    https://github.com/c-labpl/qrs_detector
    If you use these modules in a research project, please consider citing it:
    https://zenodo.org/record/583770
    If you use these modules in any other project, please refer to MIT open-source license.
    MIT License
    Copyright (c) 2017 Michał Sznajder, Marta Łukowska
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
    """

    def __init__(self):
        """
        QRSDetector class initialisation method.
        """
        # Configuration parameters.
        self.signal_frequency = 500  # Set ECG device frequency in samples per second here.

        self.number_of_samples_stored = 400  # Change proportionally when adjusting frequency (in samples).

        self.filter_lowcut = 0.1
        self.filter_highcut = 15.0
        self.filter_order = 1

        self.integration_window = 30 # Change proportionally when adjusting frequency (in samples).

        self.findpeaks_limit = 0.35
        self.findpeaks_spacing = 100  # Change proportionally when adjusting frequency (in samples).
        self.detection_window = 80  # Change proportionally when adjusting frequency (in samples).

        self.refractory_period = 200  # Change proportionally when adjusting frequency (in samples).
        self.qrs_peak_filtering_factor = 0.125
        self.noise_peak_filtering_factor = 0.125
        self.qrs_noise_diff_weight = 0.25

        # Measurements and calculated values.
        self.timestamp = 0
        self.measurement = 0
        self.detected_qrs = 0
        self.most_recent_measurements = deque([0.0], self.number_of_samples_stored)
        self.most_recent_rr_list = deque([], self.number_of_samples_stored)
        self.hrv_measures = {}
        self.samples_since_last_detected_qrs = 0
        self.qrs_peak_value = 0.0
        self.noise_peak_value = 0.0
        self.threshold_value = 0.0

    def calculate_hrv(self, rr_list):
        # Preliminary calculations needed for the different HRV calculation techniques
        rr_diff = np.diff(rr_list)
        rr_sqdiff = np.power(rr_diff, 2)
        self.hrv_measures['sdnn'] = np.std(rr_list)
        self.hrv_measures['sdsd'] = np.std(rr_diff)
        self.hrv_measures['rmssd'] = np.sqrt(np.mean(rr_sqdiff))

        return self.hrv_measures

    """ECG measurements data processing methods."""
    def process_measurement(self, raw_measurement):
        """
        Method responsible for parsing and initial processing of ECG measured data sample.
        :param str raw_measurement: ECG most recent raw measurement in "timestamp,measurement" format
        """
        self.measurement = float(raw_measurement)
        self.detected_qrs = 0
        # Appending measurements to deque used for rotating most recent samples for further analysis and detection.
        self.most_recent_measurements.append(self.measurement)
        self.detect_peaks(self.most_recent_measurements)

        # If the signal is an R peak, then append it to the list of most recent R peaks.
        if self.detected_qrs == 1:
            self.most_recent_rr_list.append(self.measurement)

        # # Call calculate_hrv function to get the three hrv calculations
        hrv_calculations = self.calculate_hrv(self.most_recent_rr_list)
        hrv_calculations['is_peak'] = self.detected_qrs

        return hrv_calculations, self.most_recent_rr_list

    def detect_peaks(self, most_recent_measurements):
        """
        Method responsible for extracting peaks from recently received ECG measurements through processing.
        :param deque most_recent_measurements: most recent ECG measurements array
        """
        # Measurements filtering - 0-15 Hz band pass filter.
        filtered_ecg_measurements = self.bandpass_filter(most_recent_measurements, lowcut=self.filter_lowcut,
                                                         highcut=self.filter_highcut, signal_freq=self.signal_frequency,
                                                         filter_order=self.filter_order)

        # Derivative - provides QRS slope information.
        differentiated_ecg_measurements = np.ediff1d(filtered_ecg_measurements)

        # Squaring - intensifies values received in derivative.
        squared_ecg_measurements = differentiated_ecg_measurements ** 2

        # Moving-window integration.
        integrated_ecg_measurements = np.convolve(squared_ecg_measurements, np.ones(self.integration_window))

        # Fiducial mark - peak detection on integrated measurements.
        detected_peaks_indices = self.findpeaks(data=integrated_ecg_measurements,
                                                limit=self.findpeaks_limit,
                                                spacing=self.findpeaks_spacing)
        detected_peaks_indices = detected_peaks_indices[
            detected_peaks_indices > self.number_of_samples_stored - self.detection_window]
        detected_peaks_values = integrated_ecg_measurements[detected_peaks_indices]

        self.detect_qrs(detected_peaks_values=detected_peaks_values)

    """QRS detection methods."""
    def detect_qrs(self, detected_peaks_values):
        """
        Method responsible for classifying detected ECG measurements peaks either as noise or as QRS complex (heart beat).
        :param array detected_peaks_values: detected peaks values array
        """
        self.samples_since_last_detected_qrs += 1

        # After a valid QRS complex detection, there is a 200 ms refractory period before next one can be detected.
        if self.samples_since_last_detected_qrs > self.refractory_period:
            # Check whether any peak was detected in analysed samples window.
            if len(detected_peaks_values) > 0:

                # Take the last one detected in analysed samples window as the most recent.
                most_recent_peak_value = detected_peaks_values[-1]

                # Peak must be classified either as a noise peak or a QRS peak.
                # To be classified as a QRS peak it must exceed dynamically set threshold value.
                if most_recent_peak_value > self.threshold_value:
                    self.handle_detection()
                    self.samples_since_last_detected_qrs = 0

                    self.detected_qrs = 1

                    # Adjust QRS peak value used later for setting QRS-noise threshold.
                    self.qrs_peak_value = self.qrs_peak_filtering_factor * most_recent_peak_value + \
                                          (1 - self.qrs_peak_filtering_factor) * self.qrs_peak_value
                else:
                    # Adjust noise peak value used later for setting QRS-noise threshold.
                    self.noise_peak_value = self.noise_peak_filtering_factor * most_recent_peak_value + \
                                            (1 - self.noise_peak_filtering_factor) * self.noise_peak_value

                # Adjust QRS-noise threshold value based on previously detected QRS or noise peaks value.
                self.threshold_value = self.noise_peak_value + \
                                       self.qrs_noise_diff_weight * (self.qrs_peak_value - self.noise_peak_value)


    def handle_detection(self):
        """
        Method responsible for generating any kind of response for detected QRS complex.
        """
        # print("Pulse")

    """Tools methods."""
    def bandpass_filter(self, data, lowcut, highcut, signal_freq, filter_order):
        """
        Method responsible for creating and applying Butterworth filter.
        :param deque data: raw data
        :param float lowcut: filter lowcut frequency value
        :param float highcut: filter highcut frequency value
        :param int signal_freq: signal frequency in samples per second (Hz)
        :param int filter_order: filter order
        :return array: filtered data
        """
        """Constructs signal filter and uses it to given data set."""
        nyquist_freq = 0.5 * signal_freq
        low = lowcut / nyquist_freq
        high = highcut / nyquist_freq
        b, a = butter(filter_order, [low, high], btype="band")
        y = lfilter(b, a, data)
        return y

    def findpeaks(self, data, spacing=1, limit=None):
        """
        Janko Slavic peak detection algorithm and implementation.
        https://github.com/jankoslavic/py-tools/tree/master/findpeaks
        Finds peaks in `data` which are of `spacing` width and >=`limit`.
        :param ndarray data: data
        :param float spacing: minimum spacing to the next peak (should be 1 or more)
        :param float limit: peaks should have value greater or equal
        :return array: detected peaks indexes array
        """
        len = data.size
        x = np.zeros(len + 2 * spacing)
        x[:spacing] = data[0] - 1.e-6
        x[-spacing:] = data[-1] - 1.e-6
        x[spacing:spacing + len] = data
        peak_candidate = np.zeros(len)
        peak_candidate[:] = True
        for s in range(spacing):
            start = spacing - s - 1
            h_b = x[start: start + len]  # before
            start = spacing
            h_c = x[start: start + len]  # central
            start = spacing + s + 1
            h_a = x[start: start + len]  # after
            peak_candidate = np.logical_and(peak_candidate, np.logical_and(h_c > h_b, h_c > h_a))

        ind = np.argwhere(peak_candidate)
        ind = ind.reshape(ind.size)
        if limit is not None:
            ind = ind[data[ind] > limit]
        return ind

    def calc_breathing(self, rrlist, sampling_freq, method='welch', filter_breathing=True,
                       bw_cutoff=[0.1, 0.4], measures={}, working_data={}):
            '''estimates breathing rate
            Function that estimates breathing rate from heart rate signal.
            Upsamples the list of detected rr_intervals by interpolation then
            tries to extract breathing peaks in the signal.
            Parameters
            ----------
            rr_list : 1d list or array
                list or array containing peak-peak intervals
            sampling_freq: integer
                value associated with the sampling frequency of the data
            method : str
                method to use to get the spectrogram, must be 'fft' or 'welch'
                default : fft
            filter_breathing : bool
                whether to filter the breathing signal derived from the peak-peak intervals
                default : True
            bw_cutoff : list or tuple
                breathing frequency range expected
                default : [0.1, 0.4], meaning between 6 and 24 breaths per minute
            measures : dict
                dictionary object used by heartpy to store computed measures. Will be created
                if not passed to function.
            working_data : dict
                dictionary object that contains all heartpy's working data (temp) objects.
                will be created if not passed to function
            Returns
            -------
            measures : dict
                dictionary object used by heartpy to store computed measures.
            Examples
            --------
            Normally this function is called during the process pipeline of HeartPy. It can
            of course also be used separately.
            Let's load an example and get a list of peak-peak intervals
            >>> import heartpy as hp
            >>> data, _ = hp.load_exampledata(0)
            >>> wd, m = hp.process(data, 100.0)
            Breathing is then computed with the function
            >>> m, wd = calc_breathing(wd['RR_list_cor'], measures = m, working_data = wd)
            >>> round(m['breathingrate'], 3)
            0.171
            There we have it, .17Hz, or about one breathing cycle in 6.25 seconds.
            '''

            #resample RR-list to 1000Hz
            x = np.linspace(0, len(rrlist), len(rrlist))
            x_new = np.linspace(0, len(rrlist), np.sum(np.asarray(rrlist), dtype=np.int32))
            interp = UnivariateSpline(x, rrlist, k=3)
            breathing = interp(x_new)
            #Using sampling frequency of 10*original sampling frequency to account for k=3 spline
            adj_sampling_frequency = sampling_freq * 10

            if filter_breathing:
                breathing = self.bandpass_filter(breathing, lowcut=bw_cutoff[0],
                                                             highcut=bw_cutoff[1], signal_freq=float(adj_sampling_frequency),
                                                             filter_order=self.filter_order)

            if method.lower() == 'fft':
                datalen = len(breathing)
                frq = np.fft.fftfreq(datalen, d=((1/float(adj_sampling_frequency))))
                frq = frq[range(int(datalen/2))]
                Y = np.fft.fft(breathing)/datalen
                Y = Y[range(int(datalen/2))]
                psd = np.power(np.abs(Y), 2)
            elif method.lower() == 'welch':
                if len(breathing) < 30000:
                    frq, psd = welch(breathing, fs=adj_sampling_frequency, nperseg=len(breathing))
                else:
                    frq, psd = welch(breathing, fs=adj_sampling_frequency, nperseg=np.clip(len(breathing) // 10,
                                                                        a_min=30000, a_max=None))
            else:
                raise ValueError('Breathing rate extraction method not understood! Must be \'welch\' or \'fft\'!')

            #find max
            measures['breathingrate'] = frq[np.argmax(psd)] * 60
            working_data['breathing_signal'] = breathing
            working_data['breathing_psd'] = psd
            working_data['breathing_frq'] = frq

            return measures, working_data
