import numpy as np

class Beamformer:
    def __init__(self, delays):
        self.delays = delays

    def apply(self, signal):
        shifted = [np.roll(signal, d) for d in self.delays]
        return np.mean(shifted, axis=0)