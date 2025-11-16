from scipy.signal import butter, filtfilt

class BandPassFilter:
    def __init__(self, fs, lowcut, highcut, order=4):
        self.fs = fs
        self.lowcut = lowcut
        self.highcut = highcut
        self.order = order
        nyquist = fs / 2
        self.b, self.a = butter(order, [lowcut / nyquist, highcut / nyquist], btype="band")

    def apply(self, signal):
        return filtfilt(self.b, self.a, signal)