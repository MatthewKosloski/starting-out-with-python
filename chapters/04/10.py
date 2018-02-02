# Program 4-10

print('This program displays a list of numbers\n' +
'(starting at 1) and their squares.')

end = int(input('How high should I go? '))

print('\nNumber\tSquares\n---------------')

for num in range(1, end + 1):
	square = num ** 2
	print(num, '\t', square)