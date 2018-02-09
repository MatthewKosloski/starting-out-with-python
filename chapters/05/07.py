# Program 5-7
# Converts cups to fluid ounces.

def main():
	intro()

	cups_needed = int(input('Enter the number of cups: '))

	cups_to_ounces(cups_needed)

def intro():
	print('This program converts measurements in cups\n' +
		'to fluid ounces.  For your reference the\n' +
		'formula is: 1 cup = 8 fluid ounces\n'
	)

def cups_to_ounces(cups):
	ounces = cups * 8
	print('That converts to', ounces, 'ounces.')

main()