# Program 4-20
# Stair-step pattern

steps = 5

for r in range(steps):
	for c in range(r):
		print(' ', end='')
	print('#')