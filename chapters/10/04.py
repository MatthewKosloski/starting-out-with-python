# Program 10-4
# This program imports the coin module and 
# creates an instance of the Coin class.

import coin

def main():
	my_coin = coin.Coin()

	print('Side facing up:', my_coin.get_sideup())

	# Toss the coin
	print('I am going to toss the coin ten times:')
	for toss in range(10):
		my_coin.toss()
		print('Toss', toss + 1, my_coin.get_sideup())

main()