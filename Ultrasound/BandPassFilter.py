from scipy.signal import butter, filtfilt

class BandPassFilter:
    SAMPLING_RATE_HZ = 10_000_000
    LOWCUT_HZ = 1_000_000
    HIGHCUT_HZ = 3_000_000
    FILTER_ORDER = 4

    def __init__(self):
        nyquist = self.SAMPLING_RATE_HZ / 2
        self.b, self.a = butter(self.FILTER_ORDER, [self.LOWCUT_HZ / nyquist, self.HIGHCUT_HZ / nyquist], btype="band")

    def apply(self, signal):
        return filtfilt(self.b, self.a, signal)