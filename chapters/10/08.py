# Program 10-8
# This program tests the CellPhone class.

import cellphone

def main():
	manufacturer = input('Enter the manufacturer: ')
	model = input('Enter the model number: ')
	retail = float(input('Enter the retail price: '))

	phone = cellphone.CellPhone(manufacturer, model, retail)

	print('Here is the data that you entered:')
	print('Manufacturer:', phone.get_manufact())
	print('Model:', phone.get_model())
	print('Retail price:', phone.get_retail_price())

main()