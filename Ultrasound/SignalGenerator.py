import numpy as np

class SignalGenerator:
    def __init__(self, fs, duration, carrier_freq, sigma, noise_level):
        self.fs = fs
        self.duration = duration
        self.carrier_freq = carrier_freq
        self.sigma = sigma
        self.noise_level = noise_level

    def generate(self):
        time = np.linspace(0, self.duration, int(self.fs * self.duration))
        pulse = np.sin(2 * np.pi * self.carrier_freq * time) * np.exp(
            -((time - self.duration / 2) ** 2) / (2 * self.sigma ** 2)
        )
        noisy = pulse + self.noise_level * np.random.randn(len(time))
        return time, noisy
