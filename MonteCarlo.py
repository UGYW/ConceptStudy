"""
Uma Wu
Math Tutorial: Monte Carlo Integration
March 4, 2016
"""
import numpy as np
import matplotlib.pyplot as plt

def f(x):
	y = 1/(1+x**2)
	return y

def MonteCarlo(f, a, b, N):
	RieSum = 0 
	selection = np.random.uniform(a, b, N) 

	for i in range(N):
		xi = np.random.choice(selection)
		RieSum += f(xi)

	integral = RieSum*(b-a)/N 
	return integral

def test(p):
	

a = 0 #Lower Bound
b = 4 #Uppter Bound
N = 100 #Number of Test Points
trials = 1000 #Number of Trials

CalcValue = 1.3258
CalcLine = np.zeros(
	trials)
CalcLine[:] = 1.3258

for n in range(trials):
	Integral = MonteCarlo(f, a, b, N)
	Error = CalcValue - Integral
	print Error
	plt.plot(n, Integral, ".b")

plt.plot(CalcLine, "r")
plt.show()
