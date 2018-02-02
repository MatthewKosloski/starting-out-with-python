# Program 4-1
# This program calculates sales commissions.

# Create a variable to control the loop
keep_going = 'y'

# Calculate a series of commissions
while keep_going == 'y':
	# Get a salesperson's sales and commission rate.
	sales = float(input('Enter the amount of sales: '))
	comm_rate = float(input('Enter the commission rate: '))

	# Calculate commission
	commission = sales * comm_rate

	# Display commission
	print('This commission is $', format(commission, ',.2f'), sep='')

	# See if the user wants to do another calculation
	keep_going = input('Do you want to calculate another ' +
		'commission? (Enter y for yes): ')