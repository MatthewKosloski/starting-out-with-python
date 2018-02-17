# This program passes a Coin object as
# an argument to a function.
import coin

def main():

	my_coin = coin.Coin()

	print(my_coin.get_sideup())

	flip(my_coin)

	print(my_coin.get_sideup())

def flip(coin):
	coin.toss()

main()

