"""
Uma Wu
10286152
Assignment 4: Markov Chain BONUS
CPSC001
March 14, 2016
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
			try:
				freq[kgram][text[(i+k)%(len(text))]] += 1
			except KeyError:
				freq[kgram][text[(i+k)%(len(text))]] = 1
		except KeyError:
			freq[kgram] = {}
			try:
				freq[kgram][text[(i+k)%(len(text))]] += 1
			except KeyError:
				freq[kgram][text[(i+k)%(len(text))]] = 1

	return freq

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

	for n in range(textlen-k):
		minilib = library[word]
		characters = []
		probs = []
		for key in minilib:
			characters.append(key)
			probs.append(minilib[key])

		total = sum(probs)
		for i in range(len(probs)):
			probs[i] = probs[i]/float(total)

		next = np.random.choice(characters, p=probs)
		generated += next
		word = generated[n+1:]
		

	return generated

library = count(script, k)
generated = randomtalk(library, k, textlen, script)
print generated