# Program 6-13
# Gets employee data from the user and 
# saves it as records in the employee.txt file.

def main():

	number_of_employees = int(input('How many employee records' + 
		'do you want to create? '))

	employee_file = open('employees.txt', 'w')

	# Get each employee's data and 
	# write it to employees.txt
	for count in range(1, number_of_employees + 1):
		print('Enter data for employee #', count, sep='')
		name = input('Name: ')
		id_num = input('ID number: ')
		dept = input('Department: ')

		employee_file.write(name + '\n')
		employee_file.write(id_num + '\n')
		employee_file.write(dept + '\n')

		print()

	employee_file.close()
	print('Employee records written to employees.txt')

main()