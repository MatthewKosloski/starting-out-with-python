# Matthew Kosloski
# Exercise 10-1
# CPSC 3310-01 SP2018

from pet import Pet

def main():

	again = 'y'

	while again.lower() == 'y':
		pet_name = input('Pet name: ')
		pet_type = input('Pet type: ')
		pet_age = input('Pet age: ')

		the_pet = Pet(pet_name, pet_type, pet_age)

		print()
		print(the_pet)

		again = input('Again? (y/n): ')

main()