import string
import random
import matplotlib.pyplot as plt
import sys
def randomword(length):
	randomword = ""
	choices = string.letters + " "
	for x in range(length):
		randomword += random.choice(choices)

	return randomword	

def guess(inString):
	outString = randomword(len(inString))
	choices = string.letters + " "
	iterations = 0

	while inString != outString:
		for n in range(len(inString)):
			if outString[n] != inString[n]:
				letter = random.choice(choices)
				outString = outString.replace(outString[n], letter, 1)
			else:
				pass
		iterations += 1
		# print outString

	# print "The length of the string is %i." %len(inString)
	# print "It took %i iterations to replicate this string." %iterations
	return iterations

trials = 10 
textlen = range(1, 101)

for i in textlen:
	average = 0
	for j in range(trials):
		command = randomword(i)
		iterations = guess(command)
		average += iterations

	average = average/iterations
	plt.plot(i, average, ".b")

plt.show()