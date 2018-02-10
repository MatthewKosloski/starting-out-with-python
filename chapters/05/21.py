# Program 5-21

def main():
	first_age = int(input('Enter your age: '))

	second_age = int(input('Enter your best friend\'s age: '))

	total = sum(first_age, second_age)

	print('Together you are both', total, 'years old.')

def sum(a, b):
	return a + b

main()