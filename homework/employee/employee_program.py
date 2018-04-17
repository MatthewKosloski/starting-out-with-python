# Matthew Kosloski
# Exercise 11-1, 11-2
# CPSC 3310-01 SP2018

from employee import Employee, ProductionWorker, ShiftSupervisor

def main():

	another = 'y'

	print_greeting()

	while another.lower() == 'y':

		# 0 = Employee, 1 = ProductionWorker, 2 = ShiftSupervisor
		choice = get_choice()
		
		print(f'\nEnter in the following fields\nto create a new "{get_employee_type_str(choice)}":\n')

		name, number = get_employee_name_number()

		# ProductionWorker (employee_type is 1)
		if choice == ProductionWorker.employee_type:
			production_worker_actions(name, number, ProductionWorker.employee_type_str)
		# ShiftSupervisor (employee_type is 2)
		elif choice == ShiftSupervisor.employee_type:
			shift_supervisor_actions(name, number, ShiftSupervisor.employee_type_str)

		# Employee (employee_type is 0)
		else:
			employee_actions(name, number, Employee.employee_type_str)

		print()
		another = input('Add another employee? (y/n): ')

def get_employee_name_number():
	name = get_valid_input(
			'Employee name: ', 
			'str', 
			lambda val: len(val) > 0, 
			'Please enter in the employee\'s name!'
		)

	number = get_valid_input(
		'Employee number: ', 
		'int', 
		lambda val: val > 0,
		'Employee number must be greater than 0!'
	)

	return name, number

def employee_actions(name, number, type_str):
	obj = Employee(name, number)
	print()
	print_generic_employee_info(obj, type_str)

def shift_supervisor_actions(name, number, type_str):
	annual_salary, annual_production_bonus = get_shift_supervisor_attributes()
	obj = ShiftSupervisor(name, number, annual_salary, annual_production_bonus)
	print_shift_supervisor_info(obj, type_str)

def production_worker_actions(name, number, type_str):
	shift, hourly_pay_rate = get_production_worker_attributes()
	obj = ProductionWorker(name, number, shift, hourly_pay_rate)
	print_production_worker_info(obj, type_str)


def print_shift_supervisor_info(obj, type_str):
	print()
	print_generic_employee_info(obj, type_str)
	print_table_of_contents([
		['Employee annual salary', f'${format_money(obj.get_annual_salary())}'],
		['Employee annual bonus', f'${format_money(obj.get_annual_production_bonus())}']
	])

def print_production_worker_info(obj, type_str):
	print()
	print_generic_employee_info(obj, type_str)
	print_table_of_contents([
		['Employee shift', obj.get_shift()], 
		['Employee hourly pay', f'${format_money(obj.get_hourly_pay_rate())}']
	])

def print_generic_employee_info(employee, employee_type_str):
	print(f'Info for new {employee_type_str}, {employee.get_name()}:')
	print_table_of_contents([
		['Employee name', employee.get_name()], 
		['Employee number', employee.get_number()]
	])

def get_employee_type_str(employee_type):
	for cls in [Employee, ProductionWorker, ShiftSupervisor]:
		if employee_type == cls.employee_type:
			employee_type_str = cls.employee_type_str
	return employee_type_str

def get_choice():
	choice = get_valid_input(
		'Type of employee to create (0, 1, or 2): ', 
		'int', 
		lambda val: val >= 0 and val <= 2,
		'Please enter either 0, 1, or 2.'
	)
	return choice

def get_shift_supervisor_attributes():
	annual_salary = get_valid_input(
		'Employee annual salary: ', 
		'float', 
		lambda val: val > 0,
		'Salary must be greater than 0!'
	)
	annual_production_bonus = get_valid_input(
		'Employee bonus: ', 
		'float', 
		lambda val: val > 0,
		'The bonus must be greater than 0!'
	)
	return annual_salary, annual_production_bonus

def get_production_worker_attributes():
	shift = get_valid_input(
		'Employee shift: ', 
		'int', 
		lambda val: val == 1 or val == 2,
		'The shift must be either 1 or 2.'
	)
	hourly_pay_rate = get_valid_input(
		'Employee hourly pay: ', 
		'float', 
		lambda val: val > 0,
		'Hourly pay must be greater than 0!'
	)
	return shift, hourly_pay_rate

def print_greeting():
	print('\nThis program allows you to create\nthe following types of employees:\n')
	print_table_of_contents([
		['Employee', Employee.employee_type], 
		['ProductionWorker', ProductionWorker.employee_type],
		['ShiftSupervisor', ShiftSupervisor.employee_type]
	])
	print()

def format_money(integer):
	return format(integer, ',.2f')

def print_table_of_contents(lists, delimeter = '.', max_width = 30):
	for list in lists:
		label, value = list[0], list[1]
		print(f'{label:{delimeter}<{max_width}}{value}')

def get_valid_input(input_label, input_type, is_valid, error_message):
	while True:
		try:
			if input_type == 'float':
				val = float(input(input_label))
			elif input_type == 'int':
				val = int(input(input_label))
			else:
				val = input(input_label)
			if is_valid(val):
				return val
			else:
				print(error_message)
		except ValueError:
			print(error_message)

main()
