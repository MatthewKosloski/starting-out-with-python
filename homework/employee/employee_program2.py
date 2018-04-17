from employee import Employee, ProductionWorker, ShiftSupervisor

class Utils:

	@staticmethod
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

class ProgramItem:

	def __init__(self, the_attrs, the_class):
		self.__attrs = the_attrs
		self.__Class = the_class
		self.__instance = None

	def instantiate(self):
		self.__instance = self.__Class(**self.get_inputs())

	def get_inputs(self):
		attr_values = {}
		for attr in self.__attrs:
			input_id, input_label, input_type = attr['input_id'], \
			attr['input_label'], attr['input_type']
			attr_values[input_id] = input(f'{input_label}: ')

			if input_type == 'float':
				attr_values[input_id] = float(attr_values[input_id])
			elif input_type == 'int':
				attr_values[input_id] = int(attr_values[input_id])

		return attr_values

	def get_output_list(self):
		output = []
		for attr in self.__attrs:
			output.append({
				'label': attr['output_label'],
				'value': getattr(self.__instance, attr['accessor'])()
			})
		return output

	def print_output(self):
		for dict in self.get_output_list():
			label, value = dict['label'], dict['value']
			print(f'{label}: {value}')

	def __str__(self):
		return self.__Class.employee_type_str

class Program:

	def __init__(self, base_attrs, items):

		self.__base_attrs = base_attrs
		self.__items = items
		self.__program_items = []

		for item in items:
			self.__program_items.append(
				ProgramItem(self.__base_attrs + item['attrs'], item['class'])
			)

		self.start()

	def get_choice(self):
		return Utils.get_valid_input(
			'Type of employee to create (0, 1, or 2): ',
			'int',
			lambda val: val >= 0 and val <= 2,
			'Please enter 0, 1, or 2.'
		)

	def instantiate_item(self, index):
		self.__program_items[index].instantiate()

	def print_item_output(self, index):
		self.__program_items[index].print_output()

	def use_item(self, index):
		print(f'\nCreate a(an) {self.__program_items[index]}:')
		self.instantiate_item(index)
		print()
		self.print_item_output(index)

	def start(self):
		another = 'y'

		while another.lower() == 'y':
			self.use_item(self.get_choice())
			another = input('Add another employee (y/n): ')

def main():

	program = Program([{
		'input_id': 'name',
		'input_label': 'Employee name',
		'input_type': 'str',
		'accessor': 'get_name',
		'output_label': 'Name'
	},
	{ 
		'input_id': 'number',
		'input_label': 'Employee number',
		'input_type': 'int',
		'accessor': 'get_number',
		'output_label': 'Number'
	}],
	[{
		'class': Employee,
		'attrs': []
	},
	{
		'class': ProductionWorker,
		'attrs': [{ 
			'input_id': 'shift',
			'input_label': 'Employee shift (1 or 2)',
			'input_type': 'int',
			'accessor': 'get_shift',
			'output_label': 'Shift'
		},
		{ 
			'input_id': 'hourly_pay_rate',
			'input_label': 'Employee hourly rate',
			'input_type': 'float',
			'accessor': 'get_hourly_pay_rate',
			'output_label': 'Hourly rate'
		}]
	},
	{
		'class': ShiftSupervisor,
		'attrs': [{ 
			'input_id': 'annual_salary',
			'input_label': 'Employee annual salary',
			'input_type': 'float',
			'accessor': 'get_annual_salary',
			'output_label': 'Annual salary'
		},
		{ 
			'input_id': 'annual_production_bonus',
			'input_label': 'Employee bonus',
			'input_type': 'float',
			'accessor': 'get_annual_production_bonus',
			'output_label': 'Bonus'
		}]
	}])

main()