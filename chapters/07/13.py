# Program 7-13
# Uses the writelines method to save 
# a list of strings to a file.

def main():

	cities = ['Boston', 'Chicago', 'New York']

	outfile = open('cities.txt', 'w')
	
	for city in cities:
		outfile.write(f'{city}\n')

	outfile.close()

main()