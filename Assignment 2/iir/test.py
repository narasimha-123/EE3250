import numpy as np
import matplotlib.pyplot as plt

c = np.loadtxt("dignum.dat")
v = np.loadtxt("digden.dat")

u = np.flip(v)

m = len(v)
K = np.zeros(m)
C = np.zeros(m)
K[m-2] = v[m-1]
C[m-1] = c[m-1]

while(m>1 and K[m-2] != 1):
	c = c - C[m-1]*u
	v = (v - (K[m-2]*u)/(1 - K[m-2]**2))
	m = m-1
	v = v[0:m]
	c = c[0:m]
	u = np.fliplr(v)
	
	if(m>1):
		K[m-2] = v[m-1]
	C[m-1] = c[m-1]

