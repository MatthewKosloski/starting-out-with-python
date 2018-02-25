# Program 6-26
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

		print('Total:', format(total, ',.2f'))

	except IOError:
		print(f'Failed to read file {filename}.')
	except ValueError:
		print(f'Non-numeric data found in file {filename}.')
	except:
		print('An error occurred.')

main()