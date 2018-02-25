# Program 6-18
# Modify coffee.txt records.

import os

def main():

	found = False

	search = input('Enter a description to search for: ')
	new_quantity = int(input('Enter the new quantity: '))

	# Open the original file
	coffee_file = open('coffee.txt', 'r')

	# Create a temporary file
	temp_file = open('temp.txt', 'w')

	description = coffee_file.readline()

	while description != '':

		quantity = float(coffee_file.readline())

		description = description.rstrip('\n')

		if description == search:
			temp_file.write(f'{description}\n')
			temp_file.write(f'{str(new_quantity)}\n')

			found = True
		else:
			temp_file.write(f'{description}\n')
			temp_file.write(f'{str(quantity)}\n')

		description = coffee_file.readline()

	coffee_file.close()
	temp_file.close()

	os.remove('coffee.txt')
	os.rename('temp.txt', 'coffee.txt')

	if found:
		print('Coffee.txt has been updated.')
	else:
		print('No results found! :(')

main()