"""
UMA GUANYUE WU
MATH TUTORIAL: INTEGRATION
JAN 22, 2016
"""
import math

def f(r):
	# r is max 5.29e-11
	pi = 3.141592654
	e = 2.71828
	p = 
	R = (1/9*math.sqrt(3))*(6 - )

def Integration(n, upper, lower, method):
	total_dx = float(upper) - float(lower)
	dx = total_dx/n
	area = 0.0

	if method == 1:
		while lower < upper:
			fx = f(lower)
			box = fx*dx
			area += box
			lower += dx

	elif method == 2:
		while lower < upper:
			fx = f(lower+dx)
			box = fx*dx
			area += box
			lower += dx

	elif method == 3:
		while lower < upper:
			fx = f(lower+dx/2.0)
			box = fx*dx
			area += box
			lower += dx

	elif method == 4:
		while lower <= upper:
			if area == 0.0:
				fx = f(lower)
				box = dx*f(lower)
				lower += dx
				area += box
			else:
				fx = (f(lower) + f(lower+dx))
				box = fx*0.5*dx
				area += box
				lower += dx
	print area

print "1: Ln"
print "2: Rn"
print "3: Mn"
print "4: Tn"
method = input("Input the method of choice.     ")
n = input("Input the desired number of steps.      ")
lower = input("Input the lower bound.     ")
upper = input("Input the upper bound.     ")

Integration(n, upper, lower, method)