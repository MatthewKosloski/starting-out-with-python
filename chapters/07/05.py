# Program 7-5
# Demonstrates the insert method
# on a list.

def main():

	names = ['Joe', 'Cameron', 'Ian', 'John', 'Robert']

	print('My list of friends:')
	print(names)

	names.insert(0, 'Kody')

	print('My list after adding an element:')
	print(names)

main()