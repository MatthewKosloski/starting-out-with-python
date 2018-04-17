# Matthew Kosloski
# Exercise 10-7 (Cash Reg)
# CPSC 3310-01 SP2018

class CashRegister():

	def __init__(self):
		self.retail_items = []

	def purchase_item(self, retail_item):
		self.retail_items.append(retail_item)

	def get_total(self):
		total = 0
		for retail_item in self.retail_items:
			total += retail_item.get_price()
		return total

	def show_items(self):

		output = f'\nThere are {self.get_quantity()} items in the register.'

		output += '\n' + self.make_row('Description:', 'Quantity:', 'Price:') + '\n'
		for retail_item in self.retail_items:
			desc = retail_item.get_description()
			quantity = str(retail_item.get_inventory_quantity())
			price = str(retail_item.get_price())

			output += self.make_row(desc, quantity, price)
			output += '\n'
		return output

	def clear(self):
		self.retail_items = []

	def get_quantity(self):
		return len(self.retail_items)

	def make_row(self, *args):
		output = ''
		for arg in args:
			output += arg.ljust(20)
		return output

