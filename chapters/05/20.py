# Program 5-20
# Simulates 10 tosses of a coin.

import random

HEADS = 1
TAILS = 2
TOSSES = 10

def main():
	for toss in range(TOSSES):
		if random.randint(HEADS, TAILS) == HEADS:
			print('Heads')
		else:
			print('Tails')

main()