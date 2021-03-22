import soundfile as sf
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

#If using termux
import subprocess
import shlex

def to_complex(field):
	field = str(field)[2:]
	field = field[0 : len(field) - 1]
	return complex(field.replace('+-', '-').replace('i', 'j'))

#Reading the soundfile 
input_signal, fs = sf.read('../Data/Sound_Noise.wav')
sampl_freq = fs
order = 4
cutoff_freq = 4000
Wn = 2 * cutoff_freq / sampl_freq
n = int(len(input_signal))
n = int(2 ** np.floor(np.log2(n)))
input_signal = input_signal[0 : n]

#Passing butterworth filter
b, a = signal.butter(order, Wn, 'low')

# Computing H(z)
w = 2 * np.pi * np.arange(n)/n

xn = np.loadtxt('../Data/xn.dat')
yn_de = np.loadtxt('../Data/yn.dat')
sf.write('../Data/Sound_de.wav', yn_de, sampl_freq)
t = np.arange(0, n / sampl_freq, 1/sampl_freq)
f1 = plt.figure()
plt.subplot(2,1,1)
plt.plot(t,xn)
plt.ylabel("x(t)")
plt.grid()
plt.title("Digital filter Input and Output through from difference equation")

plt.subplot(2,1,2)
plt.plot(t,yn_de)
plt.ylabel("y(t)")
plt.xlabel("time(t)")
plt.grid()
plt.savefig('../figs/xnyn.eps')

hndef = np.loadtxt('../Data/hndef.dat')
f2 = plt.figure()
plt.plot(t[0:100],hndef)
plt.ylabel("h(t)")
plt.xlabel("time(t)")
plt.grid()
plt.title("Impulse Response from difference equation")
plt.savefig('../figs/h(n).eps')

Xn = np.loadtxt('../Data/Xnfft.dat', converters={0: to_complex}, dtype = np.complex128, delimiter = '\n')
Hn = np.loadtxt('../Data/Hnfft.dat', converters={0: to_complex}, dtype = np.complex128, delimiter = '\n')
Xn = np.fft.fftshift(Xn)
Hn = np.fft.fftshift(Hn)
w = 2 * np.pi * np.arange(n)/n
w[0] = -np.pi
for i in range(1, n):
	w[i] = w[i - 1] + 2 * np.pi/n
	
f3 = plt.figure()
plt.subplot(2,1,1)
plt.plot(w,np.abs(Xn))
plt.ylabel("|X(jw)|")
plt.grid()
plt.title("|X(jw)| and |H(jw)| ")

plt.subplot(2,1,2)
plt.plot(w,np.abs(Hn))
plt.xlabel("w (in rad)")
plt.ylabel("|H(jw)|")
plt.grid()
plt.savefig('../figs/xnhnfft.eps')

ynfft = np.loadtxt('../Data/ynfft.dat')
Ynfft = np.loadtxt('../Data/Ynfft.dat', converters={0: to_complex}, dtype = np.complex128, delimiter = '\n')
sf.write('../Data/Sound_fft.wav', ynfft, sampl_freq)

f4 = plt.figure()
plt.plot(t,ynfft)
plt.xlabel("time")
plt.ylabel("y(t)")
plt.grid()
plt.title("y(t) obtained through fft and ifft ")
plt.savefig('../figs/ynfft.eps')
#plt.show()
#If using termux
subprocess.run(shlex.split("termux-open ../figs/xnyn.pdf"))
subprocess.run(shlex.split("termux-open ../figs/h(n).pdf"))
subprocess.run(shlex.split("termux-open ../figs/xnhnfft.pdf"))
subprocess.run(shlex.split("termux-open ../figs/ynfft.pdf"))
