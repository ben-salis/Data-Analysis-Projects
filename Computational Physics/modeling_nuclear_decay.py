#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 16:41:44 2020

@author: bensalis
"""

import matplotlib.pyplot as plt
import numpy as np


Na0 = 200
Nb0 = 5

Na_t = [Na0]
Nb_t = [Nb0]

t = [0]
dt = .1 
#dt = .05 #uncomment for last case (tauB < tauA)
lastStep = 50
#lastStep = 100 #uncomment for last case

for idx in range(lastStep):
    approxA = Na_t[idx] - (Na_t[idx]*dt)
    Na_t += [approxA]
    t += [t[idx] + dt]
    
#print(Na_t)

''' 
Just by looking at the numbers printed, I see a decay as expected 
given my analytical results. At first I allowed dt to be 1/2, but
changed it due to the drastic effect it had on the numbers. 
I then tried a really small step, dt = .01. The effect wasn't too surprising. 
On a small interval, the change in slope hardly changes between points. This 
caused a linear effect on the numbers. Finally, I settled on dt = .1, and got 
the desired numbers 
'''

#plt.plot(t, Na_t)

'''
The plot above is the normalized approximation and it strongly resembles
an exponential decay curve. Since tauA = 1 for the A species, this normalized 
curve is actually the final plot. 
'''
plt.plot(t, Na_t, 'co')
plt.xlabel("Time, (t)")
plt.ylabel("Population Count, $N_{A}$(t)")
plt.title("Approximation of $N_{A}$(t) Population")
plt.grid(b=None, which='major', axis='both')
figure25 = plt.gcf() # get current figure
figure25.set_size_inches(9, 7)
plt.show()
plt.close()

'''
Now I plotted the analytical solution I got on paper, which takes the form 
Na(t) = 200*exp(-t), against the approximation
'''

paperResult = []
for val in range(len(t)):
    paperResult += [Na0*np.exp(-t[val])]
    
    
#print(paperResult)
    
plt.plot(t,Na_t,'co', label = "Euler's Algorithm")
plt.plot(t, paperResult, 'r', label = "Analytical")
plt.xlabel("Time, (t)")
plt.ylabel("Population Count,  $N_{A}$(t)")
plt.title("Numerical vs Analytical Population Model, $N_{A}$(t)")
plt.legend()
plt.grid(b=None, which='major', axis='both')
figure25 = plt.gcf() # get current figure
figure25.set_size_inches(9, 7)
plt.show()
plt.close()




'''
Now we look for the numerical model of Nuclei B, which does change depending
on the relationship between tauA and tauB. More specifically, depending on 
whether tauB is greater, equal to, or less than 1. First we consider
tauB = tauA 
'''
tauB = 1
for idx in range(lastStep):
    approxB = Nb_t[idx] + (Na_t[idx] - (Nb_t[idx]/tauB)) * dt
    Nb_t += [approxB]
'''
Just looking at numbers, I'd guess that the population of B actually has a 
positive trend, since we know it starts with so much less than A. A's nuclei 
would increase the population of B before a decay began to take effect. 
'''
plt.plot(t, Nb_t, 'go', label = "Euler's Algorithim")
plt.xlabel("Time, (t)")
plt.ylabel("Population Count,  $N_{B}$(t)")
plt.title("Approximation of $N_{B}$(t) Population")
plt.legend()
plt.grid(b=None, which='major', axis='both')
figure25 = plt.gcf() # get current figure
figure25.set_size_inches(9, 7)
plt.show()
plt.close()

'''now I need to compare the analytical model to the numerical one. '''
analytic = []
for val in range(len(t)):
    analytic += [np.exp(-1*t[val])*(Nb0 + Na0*t[val])]
    
plt.plot(t, analytic, 'r', label = "Analytical")
plt.plot(t, Nb_t, 'go', label = "Euler's Algorithim")
plt.xlabel("Time, (t)")
plt.ylabel("Population Count,  $N_{B}$(t)")
plt.title("Numerical vs Analytical Population Model, $N_{B}$(t)")
plt.legend()
plt.grid(b=None, which='major', axis='both')
figure25 = plt.gcf() # get current figure
figure25.set_size_inches(9, 7)
plt.show()
plt.close()

'''
Looking at tauB > tauA now. I can see that original B nuclei vanishing slower 
due to the larger decay constant, meaning a shallower negative trend as the 
new B nuclei enter the population. 
'''
 
tauB2 = 10
Nb_t2 = [Nb0]
for idx in range(lastStep):
    approxB = Nb_t2[idx] + (Na_t[idx] - (Nb_t2[idx]/tauB2)) * dt
    Nb_t2 += [approxB]
    
plt.plot(t, Nb_t2, 'bo', label = "Euler's Algorithim")
plt.xlabel("Time, (t)")
plt.ylabel("Population Count,  $N_{B}$(t)")
plt.title("Approximation of $N_{B}$ Population vs time")
plt.legend()
plt.grid(b=None, which='major', axis='both')
figure25 = plt.gcf() # get current figure
figure25.set_size_inches(9, 7)
plt.show()
plt.close()

'''used mathematica to solve the ODE symbolically. the result was...'''
calculus = []
for val in range(len(t)):
    calculus += [5/9*np.exp(-t[val])*(-400 + 409*np.exp(t[val]*.9))]

    
plt.plot(t, Nb_t2, 'bo', label = "Euler's Algorithim")
plt.plot(t, calculus, 'r', label = "Analytical")
plt.xlabel("Time, (t)")
plt.ylabel("Population Count,  $N_{B}$(t)")
plt.title("Numerical vs Analytical Population Model, $N_{B}$(t)")
plt.legend()
plt.grid(b=None, which='major', axis='both')
figure25 = plt.gcf() # get current figure
figure25.set_size_inches(9, 7)
plt.show()
plt.close()

''' Now we consider our last case, in which tauB < tauA. This means a lower 
decay constant, so faster decay of the B nuclei, in spite of the positive flow
 '''


tauB3 = .1
Nb_t3 = [Nb0]


for idx in range(lastStep):
    approxB = Nb_t3[idx] + ((Na_t[idx] - (Nb_t3[idx]/tauB3)) * dt)
    Nb_t3 += [approxB]


    
plt.plot(t, Nb_t3, 'blueviolet', linestyle = "None", marker = "o", label = "Euler's Algorithim")
plt.xlabel("Time, (t)")
plt.ylabel("Population Count,  $N_{B}$(t)")
plt.title("Approximation of $N_{B}$ Population vs time")
plt.legend()
plt.grid(b=None, which='major', axis='both')
figure25 = plt.gcf() # get current figure
figure25.set_size_inches(9, 7)
plt.show()
plt.close()

mathematica= []
for val in range(len(t)):
    mathematica += [(5/9)*np.exp(-t[val]*10)*(-31 + 40*np.exp(t[val]*9))]

    
plt.plot(t, Nb_t3, 'blueviolet', linestyle = "None", marker = "o", label = "Euler's Algorithim")
plt.plot(t, mathematica, 'r', label = "Analytical")
plt.xlabel("Time, (t)")
plt.ylabel("Population Count,  $N_{B}$(t)")
plt.title("Numerical vs Analytical Population Model, $N_{B}$(t)")
plt.legend()
plt.grid(b=None, which='major', axis='both')
figure25 = plt.gcf() # get current figure
figure25.set_size_inches(9, 7)
plt.show()
plt.close()


