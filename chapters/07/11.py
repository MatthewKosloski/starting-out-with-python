# Program 7-11
# Uses a function to create a list.
# The function returns a reference to
# the list.

def main():

	numbers = get_values()
	print('The numbers in the list are', numbers)

def get_values():
	values = []

	again = 'y'

	while again.lower() == 'y':
		num = int(input('Enter a number: '))
		values.append(num)

		again = input('Add another number? (y/n): ')
		print()

	return values

main()