# Program 6-30
# Displays the total of the
# amounts in sales_data.txt.

def main():

	total = 0.0

	filename = 'sales_data.txt'

	try:
		infile = open(filename, 'r')

		for line in infile:
			amount = float(line)
			total += amount

		infile.close()
	except Exception as err:
		print(err)
	else:
		print('Total:', format(total, ',.2f'))

main()