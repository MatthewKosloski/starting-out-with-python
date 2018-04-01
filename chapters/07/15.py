# Program 7-15
# Saves a list of numbers to a txt file.

def main():

	numbers = [1, 2, 3, 4, 5]

	outfile = open('numbers.txt', 'w')

	for number in numbers:
		outfile.write(f'{str(number)}\n')

	outfile.close()

main()