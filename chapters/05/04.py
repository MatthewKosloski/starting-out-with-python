# Program 5-4
# Local variable error demo.

def main():
	get_name()
	print('Hello', name) # Error

def get_name():
	name = input('Enter your name: ')

main()