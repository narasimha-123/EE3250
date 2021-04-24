import numpy as np
import matplotlib.pyplot as plt

def cheb(N):
	v = [1, 0]
	u = [1]

	if(N == 0): 
		w = u 
		
	elif(N == 1): 
		w = v 
		
	else:
		for i in range(1,N):
			
			p = np.convolve([2, 0],v)
			m = len(p)
			n = len(u)
			w =  p + np.append(np.zeros((m-n,)),u)
			u = v
			v = w
	return w
