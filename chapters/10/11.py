# Program 10-11
# This program pickles CellPhone objects.

import pickle
import cellphone

# Constant for the filename.
FILENAME = 'cellphones.dat'

def main():

	again = 'y'

	# Open a file
	output_file = open(FILENAME, 'wb')

	# Get data from the user
	while again.lower() == 'y':
		# Get cellphone data
		man = input('Enter the manufacturer: ')
		mod = input('Enter the model number: ')
		retail = float(input('Enter the retail price: '))

		phone = cellphone.CellPhone(man, mod, retail)

		# Pickle the object and write it to the file
		pickle.dump(phone, output_file)

		again = input('Enter more phone data? (y/n): ')

	# Close the file
	output_file.close()
	print('Data was written to', FILENAME)

main()