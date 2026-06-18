import numpy as np
import soundfile as sf
import os


wav_filename = '14-41-51_103300000Hz.wav'
cf32_filename = os.path.splitext(wav_filename)[0] + '.cf32'


data, samplerate = sf.read('IQ/2026_06_16/14-41-51_103300000Hz.wav', dtype='float32')
# data shape is (N, 2) -> column 0 = I, column 1 = Q
iq = data[:, 0] + 1j * data[:, 1]

#print(iq[:10])

iq.astype(np.complex64).tofile(cf32_filename)