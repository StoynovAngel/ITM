import numpy as np

from BandPassFilter import BandPassFilter
from BeamFormer import Beamformer
from EnvelopeDetector import EnvelopeDetector
from ResultVisualizer import ResultVisualizer
from SignalGenerator import SignalGenerator

generator = SignalGenerator()
time, noisy_signal = generator.generate()

bandpass = BandPassFilter()
filtered_signal = bandpass.apply(noisy_signal)

beamformer = Beamformer()
beamformed_signal = beamformer.apply(filtered_signal)

envelope = EnvelopeDetector.detect(filtered_signal)

final_signal = envelope * beamformed_signal / np.max(np.abs(beamformed_signal))

ResultVisualizer.visualize(
    time, noisy_signal, filtered_signal, envelope, beamformed_signal, final_signal
)