import numpy as np
import soundfile as sf
from scipy import signal
import matplotlib.pyplot as plt
from matplotlib.markers import MarkerStyle
from matplotlib import patches
#If using termux
import subprocess
import shlex
#end if
poles = [0.69382+1j*0.41,0.69382-1j*0.41,
		0.56617835+1j*0.134423,0.56617835-1j*0.134423]
pr = [x.real for x in poles]
pi = [x.imag for x in poles]
zeros = [-4.9+1j*6.153,-4.9-1j*6.153,
		0.18318,5.62274677]
zr = [x.real for x in zeros]
zi = [x.imag for x in zeros]

x = np.linspace(-2,2,100)
ax = plt.subplot(111)
# Add unit circle and zero axes    
unit_circle = patches.Circle((0,0), radius=1, fill=False,color='black', ls='dashed')
ax.add_patch(unit_circle)

y1 = np.sqrt(16-x**2)
y2 = -np.sqrt(16-x**2)
plt.fill_between(x, y1, y2, color='#539ecd')

# Add circle passing through max abs(poles) and zero axes    
req_circle = patches.Circle((0,0), radius=np.max(np.abs(poles))
			, fill=True,color='white',ls='solid')
ax.add_patch(req_circle)
boundary = patches.Circle((0,0), radius=np.max(np.abs(poles))
			, fill=False,color='black',ls='solid')
ax.add_patch(boundary)

#plt.plot(zr,zi,'o',markersize=7,color='green')
plt.plot(pr,pi,'x',color='red',markersize=7)
plt.text(-0.1,0,"z=0")
plt.text(0.3,0.75,"ROC")
plt.text(0,1.1,"|z|=1")
plt.title('H(z) in z plane')
plt.xlabel('real')
plt.ylabel('Imaginary')
plt.grid()# minor
plt.axis('scaled')
plt.axis([-1.5,1.5,-1.5,1.5])
plt.savefig('../figs/ROC.eps')
#If using termux
#plt.savefig('../figs/ROC.pdf')
#plt.savefig('../figs/ROC.eps')
#subprocess.run(shlex.split("termux-open ../figs/ROC.pdf"))

#else
#plt.show()
