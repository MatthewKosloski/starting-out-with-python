# Program 6-16
# Displays coffee.txt records.

def main():
	
	coffee_file = open('coffee.txt', 'r')

	description = coffee_file.readline()

	while description != '':

		quantity = float(coffee_file.readline())

		description = description.rstrip('\n')

		print('Description:', description)
		print('Quantity:', quantity)

		description = coffee_file.readline()

	coffee_file.close()

main()
