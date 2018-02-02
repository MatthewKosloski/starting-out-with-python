# Program 4-12
# This program calculates the sum of a series
# of numbers entered by the user.

# The maximum number
max = 5

# Initialize the accumulator
total = 0

# Explain the purpose of the program
print('This program calculates the\nsum of',
max, 'numbers you will enter.\n')

# Get the numbers and accumulate them.
for counter in range(max):
	number = int(input('Enter a number: '))
	total += number

# Display total
print('Total:', total)