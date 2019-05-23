#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

##########

A1 = 1
A2 = 2
omega1 = 6
omega2 = 7

N = 64
#chebyshev iteratons
Nmax1 = 16
#fourier iteratons (number of harmonics)
Nmax2 = 10

##########


########    CHEBYSHEV   #########

tc = np.zeros(N)
xc = np.zeros(N)
fc = np.zeros(N)
ach = np.zeros(N)
fch = np.zeros(N)
difch = np.zeros(N)

for m in range(N):
    tm = 2*np.pi/N*(m)
    tc[m] = tm
    xm = np.cos(tm)
    xc[m] = xm
    fc[m] = A1*np.cos(omega1*xm) + A2*np.sin(omega2*xm)
    
af = np.real(np.fft.fft(fc))
ach[0] = af[0]/N;

for n in range(1,(15)):
    ach[n] = 2*af[n]/N
    
for m in range(N):
    tm = np.pi/(N-1)*(m)
    xm = np.cos(tm)
    xc[m] = xm
    fc[m] = A1*np.cos(omega1*xm) + A2*np.sin(omega2*xm)
    summ = 0
    for n in range(Nmax1):
        summ = summ + ach[n]*np.cos((n)*tm)
    fch[m] = summ
    difch[m] = abs(summ-fc[m])
    
plt.plot(xc, fc)
plt.scatter(xc, fch, color='r', marker='+')
plt.show()
plt.plot(xc, difch)
plt.show()

############    FOURIER    ###############

func1 = lambda t: A1*np.cos(omega1*t) + A2*np.sin(omega2*t)
t = np.arange(-1, 1, 1/N)

def fourierSeries(period, N):
    # Calculate the Fourier series coefficients up to the Nth harmonic
    result = []
    T = len(period)
    t = np.arange(T)
    for n in range(N+1):
        an = 2/T*(period * np.cos(2*np.pi*n*t/T)).sum()
        bn = 2/T*(period * np.sin(2*np.pi*n*t/T)).sum()
        result.append((an, bn))
    return np.array(result)

t_period = np.arange(-1, 1, 1/N)
F = fourierSeries(func1(t_period), Nmax2)

# plot an / bn 
plt.subplot(121); plt.stem(F[:,0])
plt.subplot(122); plt.stem(F[:,1])


plt.show()
def reconstruct(P, anbn):
    result = 0
    t = np.arange(P)
    for n, (a, b) in enumerate(anbn):
        if n == 0:
            a = a/2
        result = result + a*np.cos(2*np.pi*n*t/P) + b * np.sin(2*np.pi*n*t/P)
    return result

F = fourierSeries(func1(t_period), 100)
plt.plot(t, func1(t))
plt.scatter(t_period, reconstruct(len(t_period), F[:Nmax2,:]), marker = '+', color = 'r');
plt.show();
plt.plot(t_period, abs(reconstruct(len(t_period), F[:Nmax2,:]) - func1(t_period)));
