from pylsl import StreamInlet, resolve_stream
from functions.QRSDetectorOnline import QRSDetectorOnline


def rr_changes(rr_list, rr_list_size, queue_limit, peaks_time, counter, num_rr_skipped, queue_end, listChanged):
    if (rr_list_size < queue_limit) and (len(rr_list) > rr_list_size):
        #print("List Changed")
        rr_list_size = rr_list_size + 1
        peaks_time.append(counter)
        listChanged = True
        if rr_list_size == queue_limit:
            queue_end = rr_list[-1]
    elif len(rr_list) == queue_limit and rr_list[-1] != queue_end: #Account for deque size being reached
        listChanged = True
        peaks_time.append(counter)
        num_rr_skipped = num_rr_skipped - 1

    return rr_list_size, listChanged, queue_end, num_rr_skipped


def find_resp(resp_processing, rr_list, counter, sampling_frequency, listChanged, peaks_time, num_rr_skipped):
    if len(rr_list) < 4:
        if counter == 1:
            return 0, num_rr_skipped
    elif len(rr_list) >= 4 and counter < (sampling_frequency * 8):
        temp = list(rr_list)
        if listChanged:
            m, wd = resp_processing.calc_breathing(temp, sampling_freq=sampling_frequency)
            val = m['breathingrate']
            return val, num_rr_skipped

    elif counter >= (sampling_frequency * 8):
        if (peaks_time[-1] - peaks_time[0]) > (sampling_frequency * 8):
            num_rr_skipped = num_rr_skipped + 1
            peaks_time.pop(0)
            listChanged = True

        temp = list(rr_list)
        temp = temp[num_rr_skipped:]

        if listChanged:
            m, wd = resp_processing.calc_breathing(temp, sampling_freq=sampling_frequency)
            val = m['breathingrate']
            return val, num_rr_skipped
    return -1, num_rr_skipped
