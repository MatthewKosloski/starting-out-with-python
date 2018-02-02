# Program 4-19
# Triangle pattern of asterisks

size = 8

for r in range(size):
	for c in range(r + 1):
		print('*', end='')
	print()