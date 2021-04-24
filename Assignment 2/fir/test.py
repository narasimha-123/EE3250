import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if
L = 114
Fs = 48
const = 2*(np.pi)/Fs
delta = 0.15

F_p1 = 3 + 0.6*(L-107)
F_p2 = 3 + 0.6*(L-109)

delF = 0.3;

F_s1 = F_p1 + 0.3;
F_s2 = F_p2 - 0.3;

omega_p1 = const*F_p1
omega_p2 = const*F_p2

omega_c = (omega_p1+omega_p2)/2
omega_l = (omega_p1-omega_p2)/2

omega_s1 = const*F_s1
omega_s2 = const*F_s2
delomega = 2*np.pi*delF/Fs

A = -20*(np.log10(delta))
N = np.ceil((A-8)/(4.57*delomega))

N = 100
n = np.arange(-N,N)
#print(len(n))
hlp = np.divide(np.sin(n*omega_l),(n*np.pi))
hlp[N] = omega_l/np.pi
#The lowpass filter plot
omega = np.arange(-np.pi/2,np.pi/2+np.pi/200,np.pi/200)#-pi/2:pi/200:pi/2
Hlp = abs(np.polyval(hlp,np.exp(-1j*omega)))
plt.figure(1)
plt.plot(omega/np.pi,Hlp)
plt.xlabel('$\omega/\pi$')
plt.ylabel('$|H_{lp}(\omega)|$')
#plt.savefig('../figs/lowpass.pdf')
plt.savefig('../figs/FIR_lowpass.eps')
#subprocess.run(shlex.split("termux-open ../figs/lowpass.pdf"))
#else
plt.show()


hbp = np.multiply(2*hlp,np.cos(n*omega_c))

omega = np.arange(-np.pi/2,np.pi/2,np.pi/200)

Hbp = abs(np.polyval(hbp,np.exp(-1j*omega)))
plt.figure(2)
plt.plot(omega/np.pi,Hbp)
plt.xlabel('$\omega/\pi$')
plt.ylabel('$|H_{bp}(\omega)|$')
#plt.savefig('../figs/bandpass.pdf')
plt.savefig('../figs/FIR_bandpass.eps')
#subprocess.run(shlex.split("termux-open ../figs/bandpass.pdf"))
plt.show()

fir_coeff = hbp;
