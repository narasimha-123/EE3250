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

x,fs = sf.read('Sound_Noise.wav')
samp_freq = fs
order = 4
cutoff_freq = 4000.0
Wn = 2*cutoff_freq/samp_freq

b,a = signal.butter(order,Wn,'low')

omega = np.linspace(-np.pi,np.pi,len(x),endpoint=True)
z = np.exp(1j * omega)
H = H(z,b,a)
#subplots
plt.plot(omega,abs(H))
plt.title('Impulse Frequency Response')
plt.xlabel('$w$')
plt.ylabel('$H(jw)$')
plt.grid()# minor

#If using termux
plt.savefig('../figs/H(jw).pdf')
plt.savefig('../figs/H(jw).eps')
subprocess.run(shlex.split("termux-open ../figs/H(jw).pdf"))

#else
#plt.show()
