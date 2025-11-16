import numpy as np

from BandPassFilter import BandPassFilter
from BeamFormer import Beamformer
from EnvelopeDetector import EnvelopeDetector
from ResultVisualizer import ResultVisualizer
from SignalGenerator import SignalGenerator

SAMPLING_RATE_HZ = 10_000_000
DURATION_S = 0.0005
CARRIER_FREQ_HZ = 2_000_000
GAUSSIAN_STD_S = 30e-6
NOISE_LEVEL = 0.3

LOWCUT_HZ = 1_000_000
HIGHCUT_HZ = 3_000_000
FILTER_ORDER = 4
BEAM_DELAYS = [0, 20, 40]

generator = SignalGenerator(
    SAMPLING_RATE_HZ, DURATION_S, CARRIER_FREQ_HZ, GAUSSIAN_STD_S, NOISE_LEVEL
)
time, noisy_signal = generator.generate()

bandpass = BandPassFilter(SAMPLING_RATE_HZ, LOWCUT_HZ, HIGHCUT_HZ, FILTER_ORDER)
filtered_signal = bandpass.apply(noisy_signal)

beamformer = Beamformer(BEAM_DELAYS)
beamformed_signal = beamformer.apply(filtered_signal)

envelope, compressed = EnvelopeDetector.detect(filtered_signal)

final_signal = envelope * beamformed_signal / np.max(np.abs(beamformed_signal))

ResultVisualizer.visualize(
    time, noisy_signal, filtered_signal, envelope, beamformed_signal, final_signal
)