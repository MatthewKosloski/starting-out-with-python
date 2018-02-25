# Program 6-10
# Reads all values in the sales.txt file
# using a for loop.

def main():

	sales_file = open('sales.txt', 'r')

	for line in sales_file:
		amount = float(line)
		print(format(amount, ',.2f'))

	sales_file.close()

main()