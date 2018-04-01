# Program 7-17
# Assigns random numbers to
# a two-dimensional list.

import random

ROWS = 3
COLS = 4

def main():

	values = [
		[0, 0, 0, 0], 
		[0, 0, 0, 0], 
		[0, 0, 0, 0]
	]

	for row in range(ROWS):
		for col in range(COLS):
			values[row][col] = random.randint(1, 100)

	print(values)


main()