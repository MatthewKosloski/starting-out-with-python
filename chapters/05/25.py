# Program 5-25

import math

def main():
	# Get the length of the triangle's two sides.
	a = float(input('Enter length of side A: '))
	b = float(input('Enter length of side B: '))

	# Calculate hypotenuse
	c = math.hypot(a, b)

	print('The length of the hypotenuse is', c)

main()