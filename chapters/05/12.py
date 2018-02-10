# Program 5-12
# Demonstrates passing two string
# arguments to a function using keyword arguments.

def main():
	first_name = input('First name: ')
	last_name = input('Last name: ')
	print('Your name reversed is')
	reverse_name(last=first_name, first=last_name)

def reverse_name(first, last):
	print(last, ', ', first, sep='')

main()