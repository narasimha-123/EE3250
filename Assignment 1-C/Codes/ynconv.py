import numpy as np
import soundfile as sf
from scipy import signal
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if
from scipy import array, zeros, signal
from scipy.fftpack import fft, ifft, convolve
def conv(f, g): # Iam using this function instead of np.convolve because
	# I couldn't find direct circular convolution function
  # transform f and g to frequency domain
  F = fft(f)
  G = fft(g)
  # multiply entry-wise
  C = F * G
  # transfer C to time domain
  c = ifft(C)
  return c
x,fs = sf.read('../Data/Sound_Noise.wav')
l = len(x)
y = np.zeros(l)
samp_freq = fs
order = 4
cutoff_freq = 4000.0
Wn = 2*cutoff_freq/samp_freq
b,a = signal.butter(order,Wn,'low')

h = np.zeros(l)
h[0] = (b[0]/a[0])
h[1] = (1/a[0])*(b[1]-a[1]*h[0])
h[2] = (1/a[0])*(b[2]-a[1]*h[1]-a[2]*h[0])
h[3] = (1/a[0])*(b[3]-a[1]*h[2]-a[2]*h[1]-a[3]*h[0])
h[4] = (1/a[0])*(b[4]-a[1]*h[3]-a[2]*h[2]-a[3]*h[1]
		-a[4]*h[0])
for i in range(5,l):
	h[i] = (1/a[0])*(-a[1]*h[i-1]-a[2]*h[i-2]-a[3]*h[i-3]-
			a[4]*h[i-4])

y = np.zeros(l)
#y = np.convolve(x,h,'same')#Does linear convolution
y = conv(x,h)
sf.write('../Data/Sound_conv.wav',np.real(y),fs)
#subplots
plt.plot(np.real(y))
plt.title('Output signal')
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()# minor
plt.savefig('../figs/yn_conv.eps')
#If using termux
#plt.savefig('../figs/yn_conv.pdf')
#plt.savefig('../figs/yn_conv.eps')
#subprocess.run(shlex.split("termux-open ../figs/yn_conv.pdf"))
#else
#plt.show()

