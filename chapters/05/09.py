# Program 5-9
# Demonstrates passing two string
# arguments to a function.

def main():
	first_name = input('First name: ')
	last_name = input('Last name: ')
	print('Your name reversed is')
	reverse_name(first_name, last_name)

def reverse_name(first, last):
	print(last, ', ', first, sep='')

main()