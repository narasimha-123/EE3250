import numpy as np
import matplotlib.pyplot as plt
import math
#If using termux
import subprocess
import shlex
#end if

epsilon = np.arange(0.35,0.65,0.05)
l = len(epsilon)
plt.figure()
for N in range(4,5):
	for i in range(0,l):

		Omega = np.arange(0.01,2.01,0.01) + 0*1j

		temp = np.sqrt(1 + np.square((epsilon[i]**2)*np.cosh(N*np.arccosh(Omega))))
		H = np.divide(1,temp)
		plt.plot(Omega,H)

plt.xlabel('$\Omega$')
plt.ylabel('$|H_{a,LP}(j\Omega)|$')
plt.grid()
plt.savefig("../figs/IIR_Cheb_lp.eps")
plt.show()

