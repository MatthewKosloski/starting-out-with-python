# Program 11-12

import animals

def main():

	mammal = animals.Mammal('regular animal')
	dog = animals.Dog()
	cat = animals.Cat()

	# Display information about each one.
	print('Here are some animals and' 
		+ 'the sounds they make.')
	print('--------------------------------')
	show_mammal_info(mammal)
	print()
	show_mammal_info(dog)
	print()
	show_mammal_info(cat)
	print()
	show_mammal_info('I am a string')

def show_mammal_info(creature):
	if isinstance(creature, animals.Mammal):
		creature.show_species()
		creature.make_sound()
	else:
		print('That is not a Mammal!')

main()