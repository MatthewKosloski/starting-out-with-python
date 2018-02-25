# Program 6-21
# Divide by 0, but handle exception
# with an if statement.

def main():

	num1 = int(input('Number 1: '))
	num2 = int(input('Number 2: '))

	if num2 != 0:
		result = num1 / num2
		print(num1, 'divided by', num2, 'is', result)
	else:
		print('Cannot divide by 0.')

main()