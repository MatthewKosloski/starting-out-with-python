# Program 5-14

number = 0

def main():
	global number
	number = int(input('Enter a number: '))
	show_number()

def show_number():
	print('The number is', number)

main()