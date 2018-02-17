from pet import Pet

AGAIN = 'y'
DEBUG = False

def main():

	if not DEBUG:

		again = 'y'

		while again.lower() == AGAIN:
			pet_name = input('Pet name: ')
			pet_type = input('Pet type: ')
			pet_age = input('Pet age: ')

			the_pet = Pet(pet_name, pet_type, pet_age)

			print(the_pet)

			again = input('Again? (y/n): ')
	else:
		run_unit_tests()


def run_unit_tests():
	print('Running unit tests for Pet...\n')

	# Test mutators
	set_name_test()
	set_animal_type_test()
	set_age_test()

	# Test accessors
	get_name_test()
	get_animal_type_test()
	get_age_test()

def set_name_test():
	the_pet = Pet('Joe', 'Dog', 20)
	new_name = 'Robert'
	the_pet.set_name(new_name)
	test('set_name()', the_pet._Pet__name, new_name)

def set_animal_type_test():
	the_pet = Pet('Adam', 'Fly', 0.01)
	new_animal_type = 'Giraffe'
	the_pet.set_animal_type(new_animal_type)
	test('set_animal_type()', the_pet._Pet__animal_type, new_animal_type)

def set_age_test():
	the_pet = Pet('Cameron', 'Cat', 11)
	new_age = 12
	the_pet.set_age(new_age)
	test('set_age()', the_pet._Pet__age, new_age)

def get_name_test():
	name = 'Ian'
	the_pet = Pet(name, 'Squirrel', 4)
	test('get_name()', the_pet.get_name(), name)

def get_animal_type_test():
	animal_type = 'Shark'
	the_pet = Pet('Will', animal_type, 7)
	test('get_animal_type()', the_pet.get_animal_type(), animal_type)

def get_age_test():
	age = 199
	the_pet = Pet('John', 'Sea turtle', age)
	test('get_age()', the_pet.get_age(), age)

def test(describe, actual, expected):
	prefix = 'OK' if actual == expected else 'X'
	print('%s\n\t(%s) got: %s expected: %s' % 
		(describe, prefix, repr(actual), repr(expected)))

main()