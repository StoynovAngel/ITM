import numpy as np
from scipy.signal import hilbert

class EnvelopeDetector:
    @staticmethod
    def detect(signal):
        analytic = hilbert(signal)
        return np.abs(analytic)