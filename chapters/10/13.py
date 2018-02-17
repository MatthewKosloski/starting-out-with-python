# Program 10-13
# This program manages Contacts.

import contact
import pickle

# Global constants for menu choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# Global constant for the filename
FILENAME = 'contacts.dat'

def main():
	# Load the existing contact dictionary and
	# assign it to mycontacts.
	mycontacts = load_contacts()

	# Initialize a variable for the user's choice.
	choice = 0

	# Process menu selections until the user
	# wants to quit the program
	while choice != QUIT:

		choice = get_menu_choice()

		if choice == LOOK_UP:
			look_up(mycontacts)
		elif choice == ADD:
			add(mycontacts)
		elif choice == CHANGE:
			change(mycontacts)
		elif choice == DELETE:
			delete(mycontacts)

	# Save the mycontacts dictionary to a file.
	save_contacts(mycontacts)

def load_contacts():
	try:
		# Open the contacts.dat file.
		input_file = open(FILENAME, 'rb')

		# Unpickle the dictionary.
		contact_dct = pickle.load(input_file)

		# Close the phone_inventory.dat file.
		input_file.close()
	except IOError:
		# Could not open the file, 
		# so create an empty dictionary.
		contact_dct = {}

	return contact_dct

def get_menu_choice():
	print()
	print('Menu')
	print('---------------------------')
	print('1. Look up a contact')
	print('2. Add a new contact')
	print('3. Change an existing contact')
	print('4. Delete a contact')
	print('5. Quit the program')
	print()

	# Get the user's choice.
	choice = int(input('Enter your choice: '))

	# Validate the choice.
	while choice < LOOK_UP or choice > QUIT:
		choice = int(input('Enter a valid choice: '))

	return choice

# Looks up an item in the 
# specified dictionary.
def look_up(mycontacts):
	name = input('Enter a name: ')

	print(mycontacts.get(name, 'That name is not found.'))

def add(mycontacts):
	name = input('Name: ')
	phone = input('Phone: ')
	email = input('Email: ')

	# Create a Contact object named entry.
	entry = contact.Contact(name, phone, email)

	# If the name does not exist in the dictionary,
	# add it as a key with the entry object as the
	# associated value.
	if name not in mycontacts:
		mycontacts[name] = entry
		print('The entry has been added')
	else:
		print('That name already exists.')


# Changes an existing entry
# in the specified dictionary

def change(mycontacts):
	name = input('Enter a name: ')

	if name in mycontacts:
		phone = input('Enter the new phone number: ')
		email = input('Enter the new email address: ')

		entry = contact.Contact(name, phone, email)

		mycontacts[name] = entry
		print('Information updated.')
	else:
		print('That name is not found')

# Deletes an entry from
# the specified dictionary

def delete(mycontacts):
	name = input('Enter a name: ')

	# If name found, delete entry
	if name in mycontacts:
		del mycontacts[name]
		print('Entry deleted.')
	else:
		print('That name is not found.')

# Pickles the specified object
# and saves it to the contacts file.
def save_contacts(mycontacts):
	# Open the file for writing
	output_file = open(FILENAME, 'wb')

	# Pickle the dictionary and save it.
	pickle.dump(mycontacts, output_file)

	# Close the file
	output_file.close()

main()