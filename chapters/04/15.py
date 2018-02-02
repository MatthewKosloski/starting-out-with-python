# Program 4-15
# Calculate retail price

mark_up = 2.5
another = 'y' # Control loop

while another == 'y' or another == 'Y':
	# Get wholesale cost.
	wholesale = float(input('Enter the item\'s' +
	' wholesale cost: '))

	# Calculate retail price
	retail = wholesale * mark_up

	print('Retail price: $', format(retail, ',.2f'), sep='')

	# Again?
	another = input('Another item? (Enter y for yes): ')