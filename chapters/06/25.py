# Program 6-25
# Handles exceptions when trying
# to read from a file.

def main():

	filename = input('Enter a filename: ')

	try:
		infile = open(filename, 'r')

		contents = infile.read()

		print(contents)

		infile.close()
	except IOError:
		print(f'Failed to read file {filename}.')

main()