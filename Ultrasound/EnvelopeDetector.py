import numpy as np
from scipy.signal import hilbert

class EnvelopeDetector:
    @staticmethod
    def detect(signal):
        analytic = hilbert(signal)
        envelope = np.abs(analytic)
        compressed = np.log1p(40 * envelope)
        return envelope, compressed