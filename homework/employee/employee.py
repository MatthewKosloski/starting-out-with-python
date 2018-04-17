# Matthew Kosloski
# Exercise 11-1, 11-2
# CPSC 3310-01 SP2018

class Employee:

	employee_type = 0
	employee_type_str = 'Employee'

	def __init__(self, name, number):
		self.__name = name
		self.__number = number

	def get_name(self):
		return self.__name

	def get_number(self):
		return self.__number

	def set_name(self, name):
		self.__name = name

	def set_number(self, number):
		self.__number = number

class ProductionWorker(Employee):

	employee_type = 1
	employee_type_str = 'ProductionWorker'

	def __init__(self, name, number, shift, hourly_pay_rate):
		Employee.__init__(self, name, number)

		self.__shift = shift
		self.__hourly_pay_rate = hourly_pay_rate

	def get_shift(self):
		return self.__shift

	def get_hourly_pay_rate(self):
		return self.__hourly_pay_rate

	def set_shift(self, shift):
		self.__shift = shift

	def set_hourly_pay_rate(self, hourly_pay_rate):
		self.__hourly_pay_rate = hourly_pay_rate

class ShiftSupervisor(Employee):

	employee_type = 2
	employee_type_str = 'ShiftSupervisor'

	def __init__(self, name, number, annual_salary, annual_production_bonus):
		Employee.__init__(self, name, number)

		self.__annual_salary = annual_salary
		self.__annual_production_bonus = annual_production_bonus

	def get_annual_salary(self):
		return self.__annual_salary

	def get_annual_production_bonus(self):
		return self.__annual_production_bonus

	def set_annual_salary(self, annual_salary):
		self.__annual_salary = annual_salary

	def set_annual_production_bonus(self, annual_production_bonus):
		self.__annual_production_bonus = annual_production_bonus 
		
