from scipy.io import wavfile # scipy library to read wav files
import numpy as np
from scipy.fftpack import fft # fourier transform
from scipy.io.wavfile import write
import matplotlib.pyplot as plt
from scipy import signal
firstSound = "test.wav" # Audio File
secondSound = "Trumpet.wav"
fs, Audiodata1 = wavfile.read(firstSound)
fs2, Audiodata2 = wavfile.read(secondSound)


testSound = np.random.randint(min(Audiodata2),max(Audiodata2),size=44100)
Audiodata1 = testSound
#Audiodata2 = Audiodata2[:,1]
# Plot the audio signal in time


# spectrum
n = len(Audiodata1)
n = len(Audiodata2)
AudioFreq1 = fft(Audiodata1)
AudioFreq1 = AudioFreq1[0:int(np.ceil((n+1)/2.0))] #Half of the spectrum

AudioFreq2 = fft(Audiodata2)
AudioFreq2 = AudioFreq2[0:int(np.ceil((n+1)/2.0))] #Half of the spectrum
realf1 = AudioFreq1.real  #converting to real numbers
realf2 = AudioFreq2.real

fitness = sum(abs(realf1-realf2))

print("the fitness is ", fitness)