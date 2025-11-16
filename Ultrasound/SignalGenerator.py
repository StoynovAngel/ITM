import numpy as np

class SignalGenerator:
    SAMPLING_RATE_HZ = 10_000_000
    DURATION_S = 0.0005
    CARRIER_FREQ_HZ = 2_000_000
    GAUSSIAN_STD_S = 30e-6
    NOISE_LEVEL = 0.3

    def generate(self):
        time = np.linspace(0, self.DURATION_S, int(self.SAMPLING_RATE_HZ * self.DURATION_S))
        pulse = np.sin(2 * np.pi * self.CARRIER_FREQ_HZ * time) * np.exp(
            -((time - self.DURATION_S / 2) ** 2) / (2 * self.GAUSSIAN_STD_S ** 2)
        )
        noisy = pulse + self.NOISE_LEVEL * np.random.randn(len(time))
        return time, noisy
