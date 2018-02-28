# Matthew Kosloski
# Exercise 4-11
# CPSC 3310-01 SP2018

num = int(input('Enter a number >= 0 for factorial: '))

while num != -1:

	# Calculate and display factorial if number is >= 0
	if num >= 0:
		factorial = 1
		for i in range(1, num + 1):
			factorial *= i
			
		print('Factorial of', num, 'is', factorial)
		print()

	# Go again?
	print('Enter a number >= 0 for factorial ')
	num = int(input('or enter -1 to exit: '))