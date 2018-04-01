# Program 7-6
# Demonstrates the remove method
# on a list.

def main():

	food = ['Pizza', 'burgers', 'chips']

	print('Here are food items:')
	print(food)

	item = input('Which item should I remove? ')

	try:
		food.remove(item)

		print('Here is the revised list:')
		print(food)
	except ValueError:
		print('Item does not exist in lsit.')

main()