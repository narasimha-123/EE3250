import numpy as np
import soundfile as sf
from scipy import signal
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if

x,fs = sf.read('Sound_Noise.wav')
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
#subplots
plt.plot(h[0:100])
plt.title('Impulse Response Definition')
plt.xlabel('$n$')
plt.ylabel('$h(n)$')
plt.grid()# minor

#If using termux
plt.savefig('../figs/h(n).pdf')
plt.savefig('../figs/h(n).eps')
subprocess.run(shlex.split("termux-open ../figs/h(n).pdf"))
#else
#plt.show()
