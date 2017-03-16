#!/usr/bin/python3
# Jere Karstén
# 16.3.2017

import xml.etree.cElementTree as ET
import random
import sys
import argparse
from random import randint

##configuration
wordLength = 4
wordCount = 3
allowedChars = "!#$%&'()*+,-./:;<=>?@[\]^_{|}~"
digit = 4
multiple = 1
specialChars = 1

###############
# define arrays
wordArray=[]
filteredArray=[]

# Argument parse definition
parser = argparse.ArgumentParser(description='Create random password from finnish words.')
parser.add_argument('-l', '--length', type=int)
parser.add_argument('-c', '--count', type=int)
parser.add_argument('-d', '--digit', type=int)
parser.add_argument('-m', '--multiple', type=int)
parser.add_argument('-s', '--special', type=int)
parser.add_argument('-a', '--allowed')

# Parse arguments
args = parser.parse_args()

# Test for empty arguments and define
if args.length is not None:
	wordLength = args.length
if args.count is not None:
	wordCount = args.count
if args.digit is not None:
	digit = args.digit
if args.multiple is not None:
	multiple = args.multiple
if args.special is not None:
	specialChars = args.special
if args.allowed is not None:
	allowedChars = args.allowed

# parse XML
tree = ET.parse('sanalista_filtered.xml')
root = tree.getroot()

# read file into array
for child in root:
	wordArray.append(child.text)

# filter array by wordLength	
for word in wordArray:
	if len(word) == wordLength:
		filteredArray.append(word.capitalize())

def randomWord():
	return random.choice(filteredArray)

def randomChar():
	return random.choice(allowedChars)

# RNG
def randomWithNDigits(n):
    rangeStart = 10**(n-1)
    rangeEnd = (10**n)-1
    return randint(rangeStart, rangeEnd)


def generatePassword():
	i = 1
	global specialChars
	if specialChars > wordCount:
		specialChars = wordCount
	if specialChars > 0:
		charLotto = random.sample(range(1, wordCount + 1), specialChars)
	else:
		charLotto = [0]
	while i <= wordCount:
		if i in charLotto:
			print(randomChar(), end='')
		print(randomWord(), end='')
		i = i + 1	
		if charLotto == wordCount + 1:
			if i == wordCount +1:
				print(randomChar(), end='')
		if i == wordCount +1:
			if digit > 0:
				print(str((randomWithNDigits(digit))))
			else:
				print()		

def multipleWords():
	n = 1
	while n <= multiple:
		n = n + 1
		generatePassword()

multipleWords()