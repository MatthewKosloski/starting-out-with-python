# Exercise 5: Physics
# Matthew Kosloski

ANOTHER = 'y'

DEBUG = False

TIME_UNIT = 'Seconds'
MASS_UNIT = 'Kilograms'
DISTANCE_UNIT = 'Meters'
VELOCITY_UNIT = 'm/s'
KINETIC_ENERGY_UNIT = 'Joules'
GRAVITY = 9.8

def main():
	'''Main program function.  Ask the user for the time, 
	in seconds, that the object was dropped as well as for 
	the mass of the object, in kilograms. Display the results.
	Then, ask the user if they would like to go again.
	'''

	if not DEBUG:

		print('You will be prompted to enter in a time',
		'in seconds, \nin which an object fell and '
		'the mass, in kilograms,\nof the object. After, ' 
		'you will be provided with the \nfollowing calculations: '
		'distance, velocity, and kin-\netic energy. \n\nTo run '
		'unit tests, edit the "DEBUG" global constant.\n\n')

		another = 'y'

		while another.lower() == ANOTHER:

			drop_physics(get_time(), get_mass())

			another = input('Another? (y/n): ')

	else:
		print('Running unit tests...\n\n')
		run_unit_tests()

def get_time():
	'''Prompts the user to enter a time, in seconds,
	and returns the result as a float.

	Returns:
		time (float): time in seconds
	'''

	time = float(input('Time in seconds object was dropped: '))

	return time

def get_mass():
	'''Prompts the user to enter the mass of an object,
	in kilograms, and returns the result as a float.

	Returns:
		mass (float): mass in kilograms
	'''

	mass = float(input('Object mass in kilograms: '))

	return mass

def drop_physics(time, mass):
	'''Calculate falling distance, velocity, and kinetic energy
	from the provided time and mass inputs.  Then, output
	the time, mass, distance, velocity, and kinetic energy.

	Args:
		time (float): Time, in seconds, object was dropped
		mass (float): Mass, in kilograms, of the object

	Returns: void
	'''

	falling_distance = get_falling_distance(time)
	velocity = get_velocity(falling_distance, time)
	kinetic_energy = get_kinetic_energy(mass, velocity)

	print()

	print_items([
		{'label': 'Time', 'value': time, 'unit': TIME_UNIT},
		{'label': 'Mass', 'value': mass, 'unit': MASS_UNIT},
		{'label': 'Distance', 'value': falling_distance, 'unit': DISTANCE_UNIT},
		{'label': 'Velocity', 'value': velocity, 'unit': VELOCITY_UNIT},
		{'label': 'Kinetic energy', 'value': kinetic_energy, 'unit': KINETIC_ENERGY_UNIT}
	])

	print()

def get_falling_distance(time):
	'''Calculates the distance, in meters,
	that an object falls based on the time,
	in seconds, it was dropped.

	Uses the formula: distance = 1/2*9.8*time^2

	Args:
		time (int): Amount of time in seconds
		that the object has fallen.

	Returns:
		distance (float): distance in meters rounded to the hundreds
		place.
	'''
	distance = 0.5 * GRAVITY * (float(time)**2)

	return distance

def get_velocity(distance, time):
	'''Calculates the velocity, or how quickly the object
	moves, by dividing the distance traveled by the amount
	of time it took to travel the distance.

	Uses the formula: distance / time

	Args:
		distance (float): distance in meters rounded 
		to the hundreds place.
		time (int): distance traveled in seconds.

	Returns:
		velocity (float): velocity in meters per second rounded to the
		hundreds place.

	'''

	velocity = distance / time

	return round_hundredths(velocity)

def get_kinetic_energy(mass, velocity):
	'''Calculates the kinetic energy of an object, in joules.

	Uses the formula: 1/2*mass*velocity^2

	
	Args:
		mass (float): Mass of the object in kilograms
		velocity (float): Velocity of the moving object
		in meters per second.

	Returns:
		kinetic_energy (float): Kinetic energy in joules
		rounded to the hundreds place.

	'''

	kinetic_energy = 0.5 * mass * velocity**2

	return round_hundredths(kinetic_energy)

def left_adjust_str(str):
	'''Aligns a text string to the left.

	Args:
		str (str): String to align

	Returns:
		str: Aligned string
	'''

	return str.ljust(25, ' ')

def format_item(label, value, unit):
	'''Concatenates label, value, and unit and
	formats the value to a floating point number rounded
	to the hundreds place.  Also, the label is aligned to
	the left.
	
	Args:
		label (str): The label of the item (e.g., Time, Mass, etc.)
		value (float): The numerical value of the item
		unit (str): The units of the numerical value (e.g., Seconds, Joules, etc.)
	
	Returns:
		str: Formatted item

	'''
	return '%s %.2f %s' % (left_adjust_str(label), value, unit)

def print_items(dicts):
	'''Takes a list of dictionaries to loop over and print.
	
	Args:
		dicts (list -> dicts): A list of dictionaries describing
		the item to print.  The dictionary should have the following
		keys: label, value, unit.

	Returns: void

	'''
	for dict in dicts:
		print(format_item(dict['label'], dict['value'], dict['unit']))

def round_hundredths(num):
	'''Takes a number and rounds it to the hundredths place.

	Args:
		num (int|float): Number to round

	Returns:
		float: Rounded number

	'''
	return round(num, 2)

def run_unit_tests():
	'''
		Rudimentary unit tests that compare
		the expected result (value and datatype)
		to the actual result.
	'''
	describe('get_falling_distance()', [{
		'given': 'a float',
		'should': 'return a float',
		'expected': 17640.0,
		'actual': get_falling_distance(time=60)
	}])
	describe('get_velocity()', [{
		'given': 'a float and an int',
		'should': 'return a float',
		'expected': 83.33,
		'actual': get_velocity(distance=5000, time=60)
	}])
	describe('get_kinetic_energy()', [{
		'given': 'two floats',
		'should': 'return a float',
		'expected': 302400.0,
		'actual': get_kinetic_energy(mass=42, velocity=120)
	}])
	describe('left_adjust_str()', [{
		'given': 'a string',
		'should': 'return a string',
		'expected': 'Matthew                  ',
		'actual': left_adjust_str(str='Matthew')
	}])
	describe('format_item()', [{
		'given': 'two strings and a float',
		'should': 'return a string',
		'expected': 'Item                      123.00 Kilograms',
		'actual': format_item(label='Item', value=123.00, unit='Kilograms')
	}])
	describe('round_hundredths()', [{
		'given': 'a float',
		'should': 'return a float',
		'expected': 3.14,
		'actual': round_hundredths(num=3.141519)
	}])

def describe(unit, tests):
	'''Initiates tests on a function

	Args:
		unit (str): Title of the unit being tested
		tests (list -> dict) A list of dictionaries
	
	Returns: void
	'''

	print(unit)
	for test in tests:
		unit_test(test)
	print()

def unit_test(unit):
	'''Unit tests an individual test.
	
	Args:
		unit (dict): A dictionary with the following
		keys: given, should, expected, actual

	Returns: void
	'''

	expected = unit['expected']
	actual = unit['actual']

	if does_return_expected(expected, actual):
		print('  (OK) Given %s: should %s' % (
			unit['given'], 
			unit['should']))
	else:
		print('  (X) Expected "%s" (%s), but got "%s" (%s)' % (
			expected, 
			type_str(expected), 
			actual, 
			type_str(actual)))

def does_return_expected(expected, actual):
	'''Checks if expected returns the correct value and datatype.
	
	Args:
		expected (any): Any datatype
		actual (any): Any datatype
	
	Returns:
		bool: If both types have same value and datatype
	'''

	return is_same_value(expected, actual) and is_same_type(expected, actual)

def is_same_value(expected, actual):
	'''Checks to see if value of expected is the
	value of actual.

	Args:
		expected (any): Any datatype
		actual (any): Any datatype
	
	Returns:
		bool: If both types have same value
	'''

	return expected == actual

def is_same_type(expected, actual):
	'''Checks to see if datatype of expected is the
	same as that of actual.

	Args:
		expected (any): Any datatype
		actual (any): Any datatype
	
	Returns:
		bool: If both types have same datatypes
	'''

	return type(expected) == type(actual)

def type_str(val):
	'''Returns the type of val in string form.

	Args:
		val (any): Any datatype

	Returns:
		str: The datatype of val (e.g., str, bool, int, float, etc.)
	'''
	return type(val).__name__

main()