# Program 6-19
# Delete records from coffee.txt

import os

def main():

	found = False

	search = input('Which coffee do you want to delete? ')

	coffee_file = open('coffee.txt', 'r')

	temp_file = open('temp.txt', 'w')

	description = coffee_file.readline()

	while description != '':

		quantity = float(coffee_file.readline())

		description = description.rstrip('\n')

		if description != search:
			temp_file.write(f'{description}\n')
			temp_file.write(f'{str(quantity)}\n')
		else:
			found = True

		description = coffee_file.readline()

	coffee_file.close()
	temp_file.close()

	os.remove('coffee.txt')
	os.rename('temp.txt', 'coffee.txt')

	if found:
		print('The file has been updated.')
	else:
		print('No records have been deleted.')

main()