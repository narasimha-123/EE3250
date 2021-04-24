import numpy as np
import matplotlib.pyplot as plt
from cheb import *
from polypower import *
#If using termux
import subprocess
import shlex
#end if
epsilon = 0.4
N = 4

beta = ((np.sqrt(1+epsilon**2)+ 1)/epsilon)**(1/N)
r1 = (beta**2-1)/(2*beta)
r2 = (beta**2+1)/(2*beta)

u = [1]

for n in range(0,int(N/2)):
	phi = np.pi/2 + ((2*n + 1)*np.pi)/(2*N)
	v = [1,-2*r1*np.cos(phi),r1**2*np.cos(phi)**2+r2**2*np.sin(phi)**2]
	p = np.convolve(v,u)
	u = p

p1 = epsilon**2 * np.convolve(cheb(N),cheb(N)) + np.append(np.zeros((2*N,)),[1])

G = (abs(np.polyval(p,1j)))/(np.sqrt(1+epsilon**2))

Omega = np.arange(0,2.01,0.01)
H_stable = abs(np.divide(G,np.polyval(p,1j*Omega)))
H_cheb = abs(np.sqrt(np.divide(1,np.polyval(p1,1j*Omega))))

plt.figure()
plt.plot(Omega,H_stable,'o')
plt.plot(Omega,H_cheb)
plt.xlabel('$\Omega$')
plt.ylabel('$|H_{a,LP}(j\Omega)|$')
plt.legend(['Design','Specification'])
plt.grid()
plt.savefig("../figs/IIR_Cheb_lpDesign.eps")
plt.show()
