# Program 4-13

# Get the first lot number.
print('Enter the property lot number\nor enter 0 to end.')
lot = int(input('Lot number: '))

# Continue processing as long as
# the user does not enter lot number 0
while lot != 0:
	# Get property value
	value = float(input('Property value: '))

	# Calculate the property's tax.
	tax = value * 0.0065

	# Display the tax.
	print('Property tax: $', format(tax, ',.2f'), sep='')

	# Get the next lot number.
	print('Enter the property lot number\nor enter 0 to end.')
	lot = int(input('Lot number: '))