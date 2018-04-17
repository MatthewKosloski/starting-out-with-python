import lo_shu_magic_square

def main():

	test('sum_list_items()', lo_shu_magic_square.sum_list_items([2, 2]), 4)

	test('stringify_square()', lo_shu_magic_square.stringify_square([[0,0,0],[0,0,0],[0,0,0]]), '0 0 0\n0 0 0\n0 0 0')

	test('has_magic_right_diagonal()', lo_shu_magic_square.has_magic_right_diagonal([
		[0, 0, 5],
		[0, 5, 0],
		[5, 0, 0]
	], 3, 15), True)

	test('has_magic_left_diagonal()', lo_shu_magic_square.has_magic_left_diagonal([
		[5, 0, 0],
		[0, 5, 0],
		[0, 0, 5]
	], 3, 15), True)

	test('has_magic_cols()', lo_shu_magic_square.has_magic_cols([
		[1, 11, 3],
		[6, 2, 2],
		[8, 2, 10]
	], 3, 15), True)

	test('has_magic_rows()', lo_shu_magic_square.has_magic_rows([
		[9, 3, 3],
		[13, 2, 0],
		[1, 4, 10]
	], 3, 15), True)

	test('has_valid_cells()', lo_shu_magic_square.has_valid_cells([
		[1, 2, 3],
		[4, 5, 6],
		[7, 8, 9]
	], 3), True)

	test('get_square_size()', lo_shu_magic_square.get_square_size([[0,0,0],[0,0,0],[0,0,0]]), 3)

	test('get_magic_const()', lo_shu_magic_square.get_magic_const(3), 15)

	test('is_magic()', lo_shu_magic_square.is_magic([
		[4, 9, 2],
		[3, 5, 7],
		[8, 1, 6]
	], 3, 15), True)

def test(assertion, actual, expected):
	if actual == expected:
		print(f'(PASS) {assertion}')
	else:
		print(f'(X) {assertion}')

if __name__ == '__main__':
	main()
