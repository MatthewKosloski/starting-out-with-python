# Program 4-9

print('KPH\tMPH\n--------------')

for kph in range(60, 131, 10):
	mph = format(kph * 0.6214, ',.1f')
	print(kph, '\t', mph)