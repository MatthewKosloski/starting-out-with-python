# Program 10-12
# This program unpickles CellPhone objects.

import pickle
import cellphone

FILENAME = 'cellphones.dat'

def main():
	end_of_file = False

	input_file = open(FILENAME, 'rb')

	# Open the file.
	while not end_of_file:
		try:
			# Unpickle the next object.
			phone = pickle.load(input_file)

			# Display the cell phone data
			display_data(phone)

		except EOFError:
			# Set the flag to indicate the end
			# of the file has been reached.
			end_of_file = True

	# Close the file.
	input_file.close()

def display_data(phone):
	print('Here is the data that you entered:')
	print('Manufacturer:', phone.get_manufact())
	print('Model:', phone.get_model())
	print('Retail price: $', format(phone.get_retail_price(), ',.2f'), sep='')

main()