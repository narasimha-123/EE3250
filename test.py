
import numpy as np
import soundfile as sf
from scipy import signal
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if

x,fs = sf.read('Sound_conv.wav')
l = len(x)
y = np.zeros(l)
samp_freq = fs
order = 4
cutoff_freq = 4000.0
Wn = 2*cutoff_freq/samp_freq
b,a = signal.butter(order,Wn,'low')

plt.plot(x)
plt.title('Digital Filter Input')
plt.ylabel('$x(n)$')
plt.grid()# minor


#If using termux
#plt.savefig('../figs/xnyn.pdf')
#plt.savefig('../figs/xnyn.eps')
#subprocess.run(shlex.split("termux-open ../figs/xnyn.pdf"))

#else
plt.show()
