# Matthew Kosloski
# Exercise 7-11
# CPSC 3310-01 SP2018

'''
	Requirements for a Magic Square:

	- Each cell must contain a unique integer 
	between 1 and n^2, where n is the number
	of cells on each side.
	- The sum of all rows, cols, and diagonals
	must be equal to the magic constant: n(n^2 + 1)/2

'''

from functools import reduce

class Error(Exception):
	'''Base class for exceptions in this module.'''
	pass

class SquareSizeError(Error):
	'''Raised when the square argument provided to
		is_magic_square is a list with an unequal size
		(length of rows not equal to length of cols).
	'''
	def __init__(self, message):
		self.message = message

def main():

	valid_square = [
		[8, 1, 6],
		[3, 5, 7],
		[4, 9, 2]
	]

	invalid_square = [
		[9, 4, 1],
		[4, 7, 5],
		[6, 8, 3]
	]

	print(stringify_square(valid_square))
	print(is_lo_shu_magic_square(valid_square))
	print()
	print(stringify_square(invalid_square))
	print(is_lo_shu_magic_square(invalid_square))

'''
	Print an appropriate message that
	is predicated on the provided square
	being a Lo Shu Magic.

	@param {list} square
	@param {bool}
'''
def is_lo_shu_magic_square(square):
	try:
		size = get_square_size(square)
	except SquareSizeError as e:
		print(e)
	else:
		
		magic_const = get_magic_const(size)

		if is_magic(square, size, magic_const):
			return 'The list is a Lo Shu Magic Square.'
		else:
			return 'The list is NOT a Lo Shu Magic Square.'

'''
	Returns the magic constant for a 
	particular square size.

	@param size {list}
	@return {int}
'''
def get_magic_const(size):
	return size * (size**2 + 1)/2

'''
	If the provided square parameter is 
	a Lo Shu Magic Square.

	@param square {list}
	@param size {int}
	@param magic_const {int}
	@return {bool}
'''
def is_magic(square, size, magic_const):
	return has_valid_cells(square, size) and \
		has_magic_rows(square, size, magic_const) and \
		has_magic_cols(square, size, magic_const) and \
		has_magic_left_diagonal(square, size, magic_const) and \
		has_magic_right_diagonal(square, size, magic_const)

'''
	Get the size of the square. The size
	is the quantity of both rows and cols.
	If the number of rows does not match
	the quantity of cols in each row, an 
	exception is raised.

	@param square {list}
	@return num_rows {int}
'''
def get_square_size(square):
	num_rows = len(square)
	cols = list(map(len, square))

	if [num_rows] * num_rows == cols:
		return num_rows
	else:
		raise SquareSizeError(('The list is not a square. Make sure the'
			' quantity of rows is equal to the quantity of columns.'))

'''
	Check if each column in each
	row has a unique int between 1 and 
	n^2, where n is square size (e.g., 3).

	@param square {list}
	@param size {int}
	@return status {bool}
'''
def has_valid_cells(square, size):
	maximum = size**2 # maximum int permitted in cell
	current = 1 # current int we are checking (1-n^2)
	occurences = 0 # occurences of current int
	status = True

	while current <= maximum and status == True:
		for row in range(size):
			for col in range(size):
				if square[row][col] == current:
					occurences += 1

		if occurences <= 1:
			# Zero or one occurance of the current int.
			# So far, the square is unique. Move on
			# to the next int.
			current += 1
			occurences = 0
		else:
			# Short circuit. If there are more than 
			# 1 occurences of an int, the square is
			# not unique.
			status = False

	return status

'''
	Checks if the rows in the square
	are all equal to the magic constant.

	@param square {list}
	@param size {int}
	@param magic_const {int}
	@return {bool}
'''
def has_magic_rows(square, size, magic_const):
	row_sums = []
	for row in range(size):
		row_sums.append(0)
		for col in range(size):
			row_sums[row] += square[row][col]
	return sum_list_items(row_sums) == magic_const * size

'''
	Checks if the cols in the square
	are all equal to the magic constant.

	@param square {list}
	@param size {int}
	@param magic_const {int}
	@return {bool}
'''
def has_magic_cols(square, size, magic_const):
	col_sums = []
	for col in range(size):
		col_sums.append(0)
		for row in range(size):
			col_sums[col] += square[row][col]
	return sum_list_items(col_sums) == magic_const * size

'''
	Checks if the cols in the 
	left diagram add up to the magic constant.

	Left diagonal: [0][0], [1][1], [2][2]

	@param square {list}
	@param size {int}
	@param magic_const {int}
	@return {bool}
'''
def has_magic_left_diagonal(square, size, magic_const):
	col_sums = []
	for i in range(size):
		col_sums.append(square[i][i])
	return sum_list_items(col_sums) == magic_const

'''
	Checks if the cols in the 
	right diagram add up to the magic constant.

	Right diagonal: [0][2], [1][1], [2][0]

	@param square {list}
	@param size {int}
	@param magic_const {int}
	@return {bool}
'''
def has_magic_right_diagonal(square, size, magic_const):
	col_sums = []
	for i in range(size):
		col_sums.append(square[i][(size - 1) - i])
	return sum_list_items(col_sums) == magic_const

'''
	Returns a string representation
	of the square to be printed, etc.

	@param square {list}
	@return output {str}
'''
def stringify_square(square):
	size = get_square_size(square)

	output = ''
	for row in range(size):
		for col in range(size):
			output += '' if col == 0 else ' '
			output += str(square[row][col])
		output += '\n' if row != size - 1 else ''
	return output

'''
	Takes a list and reduces it to a single value 
	by summing the items.

	@param {list}
	@return {any}
'''
def sum_list_items(list):
	return reduce(lambda x, y: x + y, list)

if __name__ == '__main__':
	main()