"""
Brianca Washington
1001132562
"""

import numpy as np
import csv
import matplotlib.pyplot as plt 

#open the and extract the signal
with open('data-filtering.csv', 'r') as csvfile:
	info=csv.reader(csvfile)
	for row in info:
		sig= row
signal=np.ones(len(sig))
i=0
#numbers
for x in sig:
		signal[i]=x
		i=i+1
"""
LOWPASS

"""
sampling=2000
cutoff=50
L=21
M= L-1

f=cutoff/sampling
resultfilter=np.ones(L)
#find the weights
for n in range(len(resultfilter)):
	if(n== M/2):
		result= 2*f
	else:
		result= ((np.sin(2*np.pi*f*(n-(M/2))))/(np.pi*(n-(M/2))))
	resultfilter[n]=result


# convolve the signal

lowsig=np.convolve(signal,resultfilter, 'same')

# create the signals
t=np.arange(0,sampling,1)

frsig=np.cos(2*np.pi*4*(t/sampling))

# Plot the signals (ORIGINAL, FREQ SIG, APPLIED SIG)
plt.figure(1)
plt.subplot(3, 1, 1)
plt.title("original signal")
plt.plot(t, signal )

plt.subplot(3, 1, 2)
plt.title("4Hz signal")
plt.plot(t, frsig)

plt.subplot(3, 1, 3)
plt.title("application of lowpass filter")
plt.plot(t, lowsig)

plt.tight_layout()
plt.show()


"""
HIGHPASS


"""
sampling=2000
cutoff =280
L=21
M= L-1

f=cutoff/sampling
rfilter=np.ones(L)
Hsig=signal[:100]
#get values
for n in range(len(rfilter)):
	if(n== M/2):
		result=( 1 - (2*f))
	else:
		result= (-1*(np.sin(2*np.pi*f*(n-(M/2))))/(np.pi*(n-(M/2))))
	rfilter[n]=result
# Convolve signal and take the first 100

highsig=np.convolve(Hsig,rfilter)
HPF=highsig[:100]

#create the 330 Hz
t=np.arange(0,100,1)
threesig =np.cos(2*np.pi*330*(t/sampling))
# Plot the signals (ORIGINAL, FREQ SIG, APPLIED SIG)
plt.figure(2)
plt.subplot(3, 1, 1)
plt.title("original signal")
plt.plot(t, Hsig)

plt.subplot(3, 1, 2)
plt.title("330Hz signal")
plt.plot(t, threesig)

plt.subplot(3, 1, 3)
plt.title("Application of Highpass Filter")
plt.plot(HPF)
plt.tight_layout()

plt.show()