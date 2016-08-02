"""
Uma Wu
10286152
CPSC001 Assignment 2
October 12, 2015
Discussed with: Noah Bayless
"""

import sys
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats 
import math

#THE FUNCTIONS

"""
function simulating the values of a single trial
Inputs: Initial Price
        Sigma or Volatility
        Number of Time Steos
Output: Simulated Stock Prices (Array: Size = Number of Time Steps)
"""
def simulate(initial_price, sigma, number_dT):
     stock_price = initial_price
     market = np.zeros(number_dT)
     
     for t in range(0, number_dT):
        Z = np.random.randn()
        stock_price = stock_price*np.exp(-0.5*(sigma**2)+sigma*Z)
        market[t] = stock_price
     return market

"""
function smoothing an array
Inputs: Array In Need of Smoothing
        Radius of Smoothing Window
Output: a new smoothed array based on values of the old array
"""   
def smooth(array, window):  
    new_array = np.zeros(len(array))
    for m in range(0, len(array)):
        sum = 0
        for n in range(max(0, m-window), min(m+window+1, len(array))):
            sum = sum + array[n]
            left = max(0, m-window)
            right = min(m+window+1, len(array))
        new_array[m] = sum/(right-left)
    return new_array
    
"""
function inputting the Black Scholes equation
Inputs: Initial Price
        Strike Price
        Sigma or Volatiility
        Number of Time Steps
Output: Estimated Black-Scholes Value
"""
def blackScholes(initial_price, strike_price, sigma, time_steps):
    A = 1/(sigma*math.sqrt(time_steps))
    B = math.log(initial_price/strike_price)
    C = (sigma**2)/2*time_steps
    d1 = A*(B+C)
    d2 = A*(B-C)
    X = scipy.stats.norm.cdf(d1)*initial_price
    Y = scipy.stats.norm.cdf(d2)*strike_price
    BS = X - Y
    return BS
    
#################

Price_ini = float(sys.argv[1]) #Initial Price
Sigma = float(sys.argv[2]) 
steps = int(sys.argv[3]) #Number of Time Steps
StrPrice = float(sys.argv[4]) #Strike Price
Window = int(sys.argv[5]) #Smoothing Window
Replicates = int(sys.argv[6]) #Number of Replicates

#Graphing Simulated Brownian Motion
mkt = simulate(Price_ini, Sigma, steps)
x = np.zeros(steps)
for t in range(0, steps):
    x[t] = t

#Smoothing & Graphing
smooth_mkt = smooth(mkt, Window)
plt.plot(x, mkt)
plt.plot(x, smooth_mkt)
plt.xlabel("time (arbitrary units)")
plt.ylabel("stock price ($)")
plt.title("Simulated Stock Price")
plt.savefig("stockprice.pdf")

#Calculating Average of Estimated Option Price
option_av = np.zeros(Replicates)
for n in range(0, Replicates): 
    op_mkt = simulate(Price_ini, Sigma, steps)
    option_value = max(0, op_mkt[steps-1]-StrPrice)
    option_av[n] = option_value    
option_price = np.mean(option_av)
    
print "Estimated option price: %f" % option_price

#Calculating Black-Scholes Estimation
option_price_est = blackScholes(Price_ini, StrPrice, Sigma, steps)
print "Black-Scholes option price: %f" % option_price_est