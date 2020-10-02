from heartpy import heartpy as hp
import logging as log

from hrv-analysis

def calculate_hrv(raw_ecg_data, timestamps):
    # Calculate the frequency sample of the incoming data from the given timestamps list
    frequency_sample = hp.get_samplerate_mstimer(timestamps)
    # Debug statement for calculated fs value
    log.debug('FS: {}'.format(frequency_sample))

    # Preprocess the data
    filtered_ecg = preprocess_data(data=raw_ecg_data, frequency_sample=frequency_sample)
    # Debug statement for preprocessing of data
    log.debug('{} signals preprocessed'.format(len(raw_ecg_data)))


def preprocess_data(data, frequency_sample):
    # Remove baseline wander from ECG signals using Notch filter
    filtered_ecg = hp.remove_baseline_wander(raw_ecg_data=data, sample_rate=frequency_sample)
    # Enhance signal-noise ratio by emphasizing peaks
    filtered_ecg = hp.enhance_peaks(filtered_ecg)
    # Return filtered ecg data
    return filtered_ecg
