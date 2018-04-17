# Matthew Kosloski
# Exercise 10-5 (Cash Reg)
# CPSC 3310-01 SP2018

class RetailItem():

	def __init__(self, description, inventory_quantity, price):
		self.description = description
		self.inventory_quantity = inventory_quantity
		self.price = price

	def get_description(self):
		return self.description

	def get_inventory_quantity(self):
		return self.inventory_quantity

	def get_price(self):
		return self.price