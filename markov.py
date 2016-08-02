"""
Uma Wu
10286152
Assignment 4: Markov Chain
CPSC001
March 3, 2016
"""

import sys
import random
import numpy as np

k = int(sys.argv[1])
textlen = int(sys.argv[2])
filenames = sys.argv[3:]

script = ""
for i in range(len(filenames)):
	with open(filenames[i], "r") as book:
		script += book.read()

"""
INPUT:
	text: (string)
	k: (integer) length of kgrams
OUTPUT:
	freq: (dict) kgrams as keys
		kgram: 
"""
def count(text, k):
	freq = {}

	for i in range(len(text)): #For every letter, create a new kgram and set its freq of occurence = 0
		if i+k <= len(text)-1: #if i+k doesn't go over the length of the word
			kgram = text[i:(i+k)] #kgram is i to i+k
		else: #if i+k goes over the length of the word
			kgram = text[i:] + text[:(i+k)%(len(text))] #kgram is i and i+k%len
		
		try:
			freq[kgram] += text[(i+k)%(len(text))]
		except KeyError:
			freq[kgram] = ""
			freq[kgram] += text[(i+k)%(len(text))]

	return freq

"""
INPUT: 
	library: (dict)
OUTPUT:
	word: (str) a random key from the library
"""
def randword(library):
	pick = random.randint(0, len(library)) #picking a random word to start out
	n = 0
	for i in library:
		word = i
		n += 1
		if n == pick:
			break
	return word 
#Turns out I didn't have to generate a random word... I'll just leave this here.

"""
INPUT:
	library: (dict) contains all the frequencies
	k: (int) length of kgram
	textlen: (int) length of desired text
	script: input text
OUTPUT:
	generated: (string) the output text
"""
def randomtalk(library, k, textlen, script):
	generated = script[:k]
	word = generated

	for i in range(textlen-k):
		pick = np.random.choice(len(library[word]))
		next = library[word][pick]
		generated += next
		word = generated[i+1:]

	return generated


library = count(script, k)
generated = randomtalk(library, k, textlen, script)
print generated

# with open("Generated.txt", "a") as Generated:
# 	Generated.write(generated)
# 	Generated.write("\n")
# 	Generated.write("\n")




