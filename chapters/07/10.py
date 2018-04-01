# Program 7-10
# Uses a function to calculate
# the total of values in a list.

def main():

	numbers = [2, 4, 5, 7, 9, 10]

	print('The total is', get_total(numbers))

def get_total(value_list):
	total = 0
	for num in value_list:
		total += num
	return total

main()