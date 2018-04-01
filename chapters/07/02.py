# Program 7-2
# Demonstrates the `in` operator
# used with a list.

def main():

	prod_nums = ['V467', 'F120', 'Z952', 'P913']

	search = input('Enter a product number: ')

	if search in prod_nums:
		print(search, 'was found in the list.')
	else:
		print(search, 'was not found in the list.')

main()