# Program 11-10
# Demonstrates polymorphism

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

def show_mammal_info(creature):
	creature.show_species()
	creature.make_sound()

main()