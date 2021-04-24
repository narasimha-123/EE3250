import numpy as np
import matplotlib.pyplot as plt
from para import *
from lp_stable_cheb import lp_stable_cheb
from lpbp import lpbp
from bilin import bilin
#If using termux
import subprocess
import shlex
#end if
epsilon = 0.4;

[p,G_lp] = lp_stable_cheb(epsilon,N)

Omega_L = np.arange(-2,2.01,0.01)
H_analog_lp = G_lp*np.abs(np.divide(1,np.polyval(p,1j*Omega_L)))

[num,den,G_bp] = lpbp(p,Omega_0,B,Omega_p1);

Omega = np.arange(-0.65,0.66,0.01)
H_analog_bp = G_bp*np.abs(np.divide(np.polyval(num,1j*Omega),np.polyval(den,1j*Omega)))
plt.figure(1)
plt.ylabel('$|H_{a,BP}(j\Omega)|$')
plt.plot(Omega,H_analog_bp)
plt.savefig('../figs/IIR_Analogbp.eps')

[dignum,digden,G] = bilin(den,Omega_p1);

omega = np.arange(-2*np.pi/5,2*np.pi/5+np.pi/1000,np.pi/1000)
H_dig_bp = G*np.abs(np.divide(np.polyval(dignum,np.exp(-1j*omega)),np.polyval(digden,np.exp(-1j*omega))))

plt.figure()
plt.plot(omega/np.pi,H_dig_bp)
plt.xlabel('$\omega/\pi$')
plt.ylabel('$|H_{d,BP}(\omega)|$')
plt.savefig('../figs/IIR_Digitalbp.eps')
plt.show()

iir_num = G*dignum;
iir_den = digden;


