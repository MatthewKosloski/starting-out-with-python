# Program 7-4
# Demonstrates how to get the 
# index of an item in a list and then
# replace that item with a new one.

def main():

	food = ['Pizza', 'Burgers', 'Chips']

	print('Here are the items in the food list:')
	print(food)

	item = input('Which item should I change? ')

	try:
		# index of the item to replace
		item_index = food.index(item)

		# value of new item
		new_item = input(f'Enter the new value to replace "{food[item_index]}": ')

		food[item_index] = new_item

		print('Here is the revised list:')
		print(food)
	except ValueError:
		print('The item was not found in the list.')

main()