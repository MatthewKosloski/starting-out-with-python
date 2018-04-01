# Program 7-3
# Demonstrates how the append
# method can be used to add
# items to a list.

def main():

	name_list = []

	again = 'y'

	while again.lower() == 'y':

		name = input('Enter a name: ')

		name_list.append(name)

		again = input('Add another name? (y/n): ')
		print()

	print('Here are the names you entered:')
	
	for name in name_list:
		print(name)

main()