# Program 6-14
# Displays the records that are
# in the employees.txt file.

def main():

	employee_file = open('employees.txt', 'r')

	name = employee_file.readline()

	while name != '':

		id_num = employee_file.readline()
		dept = employee_file.readline()

		# Strip the newlines from the fields.
		name = name.rstrip('\n')
		id_num = id_num.rstrip('\n')
		dept = dept.rstrip('\n')

		print('Name:', name)
		print('ID:', id_num)
		print('Department:', dept)

		name = employee_file.readline()

	employee_file.close()

main()