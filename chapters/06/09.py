# Program 6-9
# Reads all values in the sales.txt file

def main():

	sales_file = open('sales.txt', 'r')

	line = sales_file.readline()

	while line != '':
		amount = float(line)

		print(format(amount, ',.2f'))

		line = sales_file.readline()

	sales_file.close()

main()