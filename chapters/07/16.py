# Program 7-16
# Reads a file of numbers

def main():

	infile = open('numbers.txt', 'r')

	# contents of numbers.txt in a list
	numbers = infile.readlines()

	infile.close()

	# removing terminating new line character
	index = 0
	while index < len(numbers):
		numbers[index] = int(numbers[index])
		index += 1

	print(numbers)

main()