# Program 10-3
# The Coin class simulates a coin that
# can be flipped.

import random

class Coin:

	def __init__(self):
		self.__sideup = 'Heads'

	def toss(self):
		if random.randint(0, 1) == 0:
			self.__sideup = 'Heads'
		else:
			self.__sideup = 'Tails'

	def get_sideup(self):
		return self.__sideup

def main():
	my_coin = Coin()

	print('This side is facing up:', my_coin.get_sideup())

	print('I am going to toss the coin ten times:')
	for toss in range(10):
		my_coin.toss()
		print('Toss', toss + 1, my_coin.get_sideup())

main()