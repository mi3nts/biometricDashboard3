from pylsl import StreamInlet, resolve_stream
import time
from QRSDetectorOnline import QRSDetectorOnline

print("looking for stream...")
streams = resolve_stream()
inlet = StreamInlet(streams[0])
ecg_processing = QRSDetectorOnline()
while True:
    # get a new sample (you can also omit the timestamp part if you're not
    # interested in it)
    sample, timestamp = inlet.pull_sample()
    ecg_signal = sample[68]
    rr_list = ecg_processing.process_measurement(ecg_signal)
    if len(rr_list) > 1:
        current_hrv = ecg_processing.calculate_hrv(rr_list)
        print(current_hrv)
    time.sleep(0.1)

