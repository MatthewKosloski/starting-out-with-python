# Program 6-6
# Demonstrates how numbers
# must be converted to strings
# before they are written to a 
# text file.

def main():

	outfile = open('numbers.txt', 'w')

	num1 = int(input('Number 1: '))
	num2 = int(input('Number 2: '))
	num3 = int(input('Number 3: '))

	outfile.write(str(num1) + '\n')
	outfile.write(str(num2) + '\n')
	outfile.write(str(num3) + '\n')

	outfile.close()
	print('Data written to numbers.txt.')

main()