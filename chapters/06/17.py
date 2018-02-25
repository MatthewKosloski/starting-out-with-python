# Program 6-17
# Search coffee.txt for records
# matching a description.

def main():

	found = False

	search = input('Enter a description to search for: ')

	coffee_file = open('coffee.txt', 'r')

	description = coffee_file.readline()

	while description != '':

		quantity = float(coffee_file.readline())

		description = description.rstrip('\n')

		# Determine whether this record
		# matches the search value:
		if description == search:
			print('Description:', description)
			print('Quantity:', quantity)
			print()
			found = True

		description = coffee_file.readline()

	coffee_file.close()

	if not found:
		print('No results found. :(')

main()