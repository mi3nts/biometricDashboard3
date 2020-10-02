"""
ABANDONED APPROACH. ATTEMPTED TO DO LIVE R PEAK DETECTION USING HEARTPY LIBRARY
"""

from heartpy import heartpy as hp

'''
Working data keys: ['hr', 'peaklist', 'ybeat', 'rolling_mean', 'RR_list', 'RR_indices', 'RR_diff', 'RR_sqdiff', 'rrsd', 'best', 'removed_beats', 'removed_beats_y', 
'binary_peaklist', 'RR_masklist', 'RR_list_cor', 'nn20', 'nn50', 'poincare', 'breathing_signal', 'breathing_psd', 'breathing_frq']

Measures keys: ['bpm', 'ibi', 'sdnn', 'sdsd', 'rmssd', 'pnn20', 'pnn50', 'hr_mad', 'sd1', 'sd2', 's', 'sd1/sd2', 'breathingrate']
'''

def calculate_hrv(raw_ecg_data, timestamps, hr_data):
    # Calculate the frequency sample of the incoming data from the given timestamps list
    frequency_sample = 50
    # Debug statement for calculated fs value
    print('FS: {}'.format(frequency_sample))

    # Preprocess the data
    filtered_ecg = preprocess_data(data=raw_ecg_data, frequency_sample=frequency_sample)
    # Debug statement for preprocessing of data
    print('{} signals preprocessed'.format(len(raw_ecg_data)))

    # Process the filtered data
    working_data, measures = hp.process(hrdata=filtered_ecg, sample_rate=frequency_sample)

    # TODO: Do something with HR data

    return {
        'sdnn': measures['sdnn'],
        'sdsd': measures['sdsd'],
        'rmssd': measures['rmssd'],
        'pnn20': measures['pnn20'],
        'pnn50': measures['pnn50']
    }


def preprocess_data(data, frequency_sample):
    # # Remove baseline wander from ECG signals using Notch filter
    # filtered_ecg = hp.remove_baseline_wander(data=data, sample_rate=frequency_sample)
    # # Debug baseline wander
    # print('Remove baseline wander from ECG data')

    # Enhance signal-noise ratio by emphasizing peaks
    filtered_ecg = hp.enhance_peaks(hrdata=data)
    # Debug enhance peaks
    print('Enhance ECG signal peaks')

    # Return filtered ecg data
    return filtered_ecg
