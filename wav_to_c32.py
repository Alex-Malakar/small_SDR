import numpy as np
import soundfile as sf
import os

# Input WAV file recorded by SDR software (stores IQ data as stereo audio)
wav_filename = '14-41-51_103300000Hz.wav'

# Build the output filename by swapping .wav extension for .cf32
# cf32 = Complex Float 32-bit, a raw IQ binary format GNU Radio and SDR tools read natively
cf32_filename = os.path.splitext(wav_filename)[0] + '.cf32'

# Read the WAV file as 32-bit float samples
# SDR software encodes IQ as stereo: left channel = I, right channel = Q
# samplerate will reflect the sample rate the radio was running at capture time
data, samplerate = sf.read('IQ/2026_06_16/14-41-51_103300000Hz.wav', dtype='float32')

# data arrives as shape (N, 2) — N samples, 2 columns
# Column 0 = I (in-phase), Column 1 = Q (quadrature)
# Combine into a single array of complex numbers: I + jQ
iq = data[:, 0] + 1j * data[:, 1]

# Optional debug line — prints first 10 complex samples to verify conversion
#print(iq[:10])

# Cast to complex64 (32-bit float I + 32-bit float Q) and write as raw binary
# This .cf32 file can now be loaded directly into GNU Radio, SDR#, or inspectrum
iq.astype(np.complex64).tofile(cf32_filename)
