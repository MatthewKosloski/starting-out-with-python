# Program 5-19

import random

MIN = 1
MAX = 6

def main():

	again = 'y'

	while again.lower() == 'y':
		print('Rolling the dice...')
		print('Their values are:')
		print(random.randint(MIN, MAX))
		print(random.randint(MIN, MAX))

		# go again?
		again = input('Roll again? (y = yes): ')

main()