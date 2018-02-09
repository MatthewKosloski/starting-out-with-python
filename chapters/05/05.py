# Program 5-5
# Demonstrates two functions that
# have local variables with the same name.

def main():

	texas()
	california()

def texas():
	birds = 5000
	print('Texas has', birds, 'birds.')

def california():
	birds = 8000
	print('California has', birds, 'birds.')

main()