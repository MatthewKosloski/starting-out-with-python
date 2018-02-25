# Program 6-2
# Reads and displays the contents
# of philosophers.txt.

def main():
	# Open a file
	infile = open('philosophers.txt', 'r')

	file_contents = infile.read()

	infile.close()

	print(file_contents)

main()