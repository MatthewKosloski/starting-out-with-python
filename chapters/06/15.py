# Program 6-15
# Adds records to coffee.txt.

def main():

	another = 'y'

	coffee_file = open('coffee.txt', 'a')

	while another.lower() == 'y':
		print('Enter the following coffee data:')
		description = input('Description: ')
		quantity = int(input('Quantity (in pounds): '))

		coffee_file.write(f'{description}\n')
		coffee_file.write(f'{str(quantity)}\n')

		another = input('Add another record? (y/n): ')

	coffee_file.close()
	print('Data appended to coffee.txt.')

main()