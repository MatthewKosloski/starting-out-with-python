# Program 10-2
# The Coin class simulates a coin that
# can be flipped.

import random

class Coin:

	def __init__(self):
		self.sideup = 'Heads'

	def toss(self):
		if random.randint(0, 1) == 0:
			self.sideup = 'Heads'
		else:
			self.sideup = 'Tails'

	def get_sideup(self):
		return self.sideup

def main():
	my_coin = Coin()

	print('This side is facing up:', my_coin.get_sideup())

	print('I am tossing the coin...')
	my_coin.toss()

	# I'm going to cheat and directly change the object's
	# sideup attribute.
	my_coin.sideup = 'Heads'

	print('This side is facing up:', my_coin.get_sideup())

main()