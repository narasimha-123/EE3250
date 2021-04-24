import numpy as np
import matplotlib.pyplot as plt

def polypower(v,N):
	y = [1]
	if (N > 0):
		for i in range(0,N):
			y = np.convolve(y,v)
	return y
