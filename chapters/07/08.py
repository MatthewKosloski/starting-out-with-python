# Program 7-8
# Calculates the total of the values
# in a list.

def main():
	numbers = [2, 4, 6, 8, 10]

	total = 0

	for value in numbers:
		total += value

	print('The total is', total)

main()