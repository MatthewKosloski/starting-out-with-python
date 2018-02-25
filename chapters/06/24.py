# Program 6-24
# Displays the contents of a file.

def main():

	filename = input('Enter a filename: ')

	infile = open(filename, 'r')

	contents = infile.read()

	print(contents)

	infile.close()

main()