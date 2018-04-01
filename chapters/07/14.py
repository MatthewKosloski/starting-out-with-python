# Program 7-14
# Reads a file's contents into a list.

def main():

	infile = open('cities.txt', 'r')

	# contents of cities.txt in a list
	cities = infile.readlines()

	infile.close()

	# removing terminating new line character
	index = 0
	while index < len(cities):
		cities[index] = cities[index].rstrip('\n')
		index += 1

	print(cities)

main()