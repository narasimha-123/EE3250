import numpy as np
import soundfile as sf
from scipy import signal
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if
def H(z,num,den):
    Num = np.polyval(num,pow(z,-1))
    Den = np.polyval(den,pow(z,-1))
    return Num/Den

input_signal,fs = sf.read('Sound_Noise.wav')
samp_freq = fs
order = 4
cutoff_freq = 4000.0
Wn = 2*cutoff_freq/samp_freq

b,a = signal.butter(order,Wn,'low')

x = input_signal
l = len(x)
y = np.zeros(l)

w = np.linspace(-np.pi,np.pi,len(x),endpoint=True)
z = np.exp(1j * w)
H = H(z,b,a)
X = np.fft.fftshift(np.fft.fft(x))
Y = np.multiply(X,H)
y = np.fft.ifft(np.fft.ifftshift(Y))
sf.write('Sound_fft.wav',np.real(y),fs)

plt.plot(np.real(y))
plt.title('Output signal through IFFT')
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()# minor

#If using termux
plt.savefig('../figs/ynfft.pdf')
plt.savefig('../figs/ynfft.eps')
subprocess.run(shlex.split("termux-open ../figs/ynfft.pdf"))
#else
#plt.show()
