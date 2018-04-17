# Matthew Kosloski
# Exercise Cash Reg
# CPSC 3310-01 SP2018

from cashregister import CashRegister
from retailitem import RetailItem

def main():

	def input_retail_item():
		description = input('Retail item description: ')
		inventory_quantity = int(input('Retail item inventory quantity: '))
		price = float(input('Retail item price: '))

		return description, inventory_quantity, price

	def purchase_item(description, inventory_quantity, price):
		register.purchase_item(RetailItem(description, inventory_quantity, price))

	another = 'y'
	register = CashRegister()

	print((
		'\nThis program is a cash register simulator. You\n' + 
		'will first be prompted to type a description,\n' +
		'inventory quantity, and a price for a retail\n' +
		'item. You can continue to add as many products\n' +
		'as necessary. When you are finished, the items\n' +
		'in the register, along with the total price of\n' +
		'all the items, will be displayed.\n'
	))

	while another.lower() == 'y':
		description, inventory_quantity, price = input_retail_item()
		purchase_item(description, inventory_quantity, price)
		another = input('Purchase another item? (y/n): ')

	print(register.show_items() + '\n')
	print('Total price: $', format(register.get_total(), ',.2f'), sep='')


main()