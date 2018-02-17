# Program 10-9
# The program creates three CellPhone objects and
# stores them in a list.

from cellphone import CellPhone

def main():
	# Get a list of CellPhone objects
	phones = make_list()

	# Display the data in the list.
	print('Here is the data you entered:')
	display_list(phones)

def make_list():
	phone_list = []

	print('Enter data for three phones.')
	for count in range (1, 4):
		# Get the phone data.
		print('Phone number ' + str(count) + ':')
		manufacturer = input('Manufacturer: ')
		model = input('Model: ')
		price = float(input('Retail price: '))
		print()

		phone = CellPhone(manufacturer, model, price)

		phone_list.append(phone)

	return phone_list

def display_list(phone_list):
	for phone in phone_list:
		print(phone.get_manufact())
		print(phone.get_model())
		print(phone.get_retail_price())
		print()

main()



