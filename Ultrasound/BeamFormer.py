import numpy as np

class Beamformer:
    BEAM_DELAYS = [0, 20, 40]

    def apply(self, signal):
        shifted = [np.roll(signal, d) for d in self.BEAM_DELAYS]
        return np.mean(shifted, axis=0)