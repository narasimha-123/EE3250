import soundfile as sf
import numpy as np
from scipy import signal

#If using termux
import subprocess
import shlex

#Reading the soundfile 
input_signal, fs = sf.read('../Data/Sound_Noise.wav')
sampl_freq = fs
order = 4
cutoff_freq = 4000
n = int(len(input_signal))
n = int(2 ** np.floor(np.log2(n)))
f = open("../Data/x.dat", "w")
for i in range(n):
    f.write(str(input_signal[i]) + "\n")
f.close()

Wn = 2 * cutoff_freq / sampl_freq
input_signal = input_signal[0 : n]

#Passing butterworth filter
b, a = signal.butter(order, Wn, 'low')

# Computing H(z)
w = 2 * np.pi * np.arange(n)/n
z = np.exp(-1j * w)
H = np.polyval(b, z)/np.polyval(a, z)
Hmag = np.sqrt((H.real ** 2)+(H.imag ** 2))
f1 = open("../Data/H.dat", "w")
f2 = open("../Data/Hmag.dat","w")
for i in range(n):
    f1.write(str(H[i].real) + " " + str(H[i].imag) + "\n")
    f2.write(str(Hmag[i]) + "\n")
f.close()
f1.close()
f2.close()
