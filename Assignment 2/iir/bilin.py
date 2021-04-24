import numpy as np
from add import add
from polypower import polypower

def bilin(p,om):
	p = np.array(p)
	N = p.shape[0]
	const = np.array([-1,1])
	v = 1
	if(N > 2):
		for i in range(1,N):
			v = np.convolve(v,const)
			v = add(v, p[i]*polypower([1,1],i))
		
		digden = v

	elif(N == 2):
		M = v.shape[0]
		v[M-2] = v[M-2] + p[N-1]
		v[M-1] = v[M-1] + p[N-1]
		digden = v
	
	else:
		digden = p
	
	dignum = polypower([-1,0,1],int((N-1)/2))
	G_bp = np.abs(np.polyval(digden,np.exp(-1j*om))/np.polyval(dignum,np.exp(-1j*om)))
	
	return dignum,digden,G_bp
