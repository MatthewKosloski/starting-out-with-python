# Program 4-11
# This program uses a loop to display a 
# table of numbers and their squares.

print('This program displays a list of numbers and their squares.')

start = int(input('Start at: '))
end = int(input('End at: '))

print('\nNumber\tSquares\n---------------')

for num in range(start, end + 1):
	square = num ** 2
	print(num, '\t', square)