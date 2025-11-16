import matplotlib.pyplot as plt

class ResultVisualizer:
    @staticmethod
    def visualize(time, noisy_signal, filtered_signal, envelope, beamformed_signal, final_signal):
        plt.figure(figsize=(12, 12))

        plt.subplot(5, 1, 1)
        plt.title("1. Raw Ultrasound Signal (with Noise)")
        plt.plot(time * 1e6, noisy_signal, color="gray", label="Noisy Signal")
        plt.xlabel("Time [µs]")
        plt.ylabel("Amplitude")
        plt.legend()

        plt.subplot(5, 1, 2)
        plt.title("2. Band-pass Filtered Signal")
        plt.plot(time * 1e6, filtered_signal, color="blue", label="Filtered")
        plt.xlabel("Time [µs]")
        plt.ylabel("Amplitude")
        plt.legend()

        plt.subplot(5, 1, 3)
        plt.title("3. Beamformed Signal (Delay-and-Sum)")
        plt.plot(time * 1e6, beamformed_signal, color="purple", label="Beamformed")
        plt.xlabel("Time [µs]")
        plt.ylabel("Amplitude")
        plt.legend()

        plt.subplot(5, 1, 4)
        plt.title("4. Detected Envelope (Hilbert Transform)")
        plt.plot(time * 1e6, envelope, color="orange", linewidth=2, label="Envelope")
        plt.xlabel("Time [µs]")
        plt.ylabel("Amplitude")
        plt.legend()

        plt.subplot(5, 1, 5)
        plt.title("5. Final Processed Signal (Envelope × Beamformed)")
        plt.plot(time * 1e6, final_signal, color="red", label="Processed Signal")
        plt.xlabel("Time [µs]")
        plt.ylabel("Amplitude")
        plt.legend()

        plt.tight_layout()
        plt.show()