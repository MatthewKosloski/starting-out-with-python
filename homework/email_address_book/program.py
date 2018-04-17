from email_address_book import EmailAddressBook

def main():

	def create_ordered_list(items):
		output = ''
		for item in items:
			current_index = items.index(item)

			output += str(current_index)
			output += '. '
			output += item
			# Don't append a newline after the last list item
			output += ('' if current_index == (len(items)) else '\n')
		return output

	# Views
	MAIN_VIEW = 'MainView'
	CREATE_ADDRESS_VIEW = 'CreateAddressView'
	LOOKUP_ADDRESS_VIEW = 'LookUpAddressView'
	UPDATE_ADDRESS_VIEW = 'UpdateAddressView'
	DELETE_ADDRESS_VIEW = 'DeleteAddressView'
	View_ALL_ADDRESSES_VIEW = 'ViewAllAddressesView'

	# Events
	USER_CHOICE_EVENT = 'user_choice'

	class Model():

		def __init__(self):
			self.__book = EmailAddressBook('db.dat')

		def create(self, first_name, last_name, email):
			return self.__book.create(first_name, last_name, email)

		def read(self, first_name, last_name):
			return self.__book.read(first_name, last_name)

		def update(self, first_name, last_name, email):
			return self.__book.update(first_name, last_name, email)

		def delete(self, first_name, last_name):
			return self.__book.delete(first_name, last_name)

		def write(self):
			self.__book.write_binary()

		def get(self):
			return self.__book.get_book()

	class BaseView():

		def __init__(self, name, controller):
			self.__name = name
			self.__controller = controller
			self.__choices = ['Exit Program']

		def get_name(self):
			return self.__name

		def get_controller(self):
			return self.__controller

		def set_choices(self, choices):
			self.__choices += choices

		def get_choices(self):
			return create_ordered_list(self.__choices)

		def send_data_to_controller(self, event, payload):
			data = {
				'origin': self.__name,
				'event': event,
				'payload': payload
			} 
			self.__controller.on_receive_data_from_view(data)

		def handle_choice(self, choice):
			payload = {'choice': choice}
			self.send_data_to_controller(USER_CHOICE_EVENT, payload)
			if choice == 0:
				print('Data saved to binary.')

		def choice_prompt(self):
			choice = -1
			minimum = 0
			maximum = len(self.__choices) - 1

			while not (choice >= minimum and choice <= maximum):
				try:
					choice = int(input('> '))
				except ValueError as e:
					print(f'Please enter an integer between {minimum} and {maximum}.')

			self.handle_choice(choice)

		def name_prompt(self):
			first_name = input('First Name: ')
			last_name = input('Last Name: ')
			return first_name, last_name

		def email_prompt(self):
			return input('Email Address: ')

	class MainView(BaseView):

		def __init__(self, name, controller):
			super().__init__(name, controller)

			self.set_choices([
				'Create New Address',
				'Look Up Address',
				'Update Address',
				'Delete Address',
				'View All Addresses'
			])

		def render(self):
			print()
			print()
			print('Email Address Book')
			print('This application allows you to view\nand store email addresses' + 
				' belonging to people.')
			print()
			print(self.get_choices())
			print()
			self.choice_prompt()

	class CreateAddressView(BaseView):

		def __init__(self, name, controller):
			super().__init__(name, controller)

		def render(self):
			print()
			print()
			print('Create new email address:')
			print()

			first_name, last_name = self.name_prompt()
			email = self.email_prompt()

			results = (self.get_controller()
				.create_email_address(first_name, last_name, email))

			print()
			if results:
				print(f'Email {email} belonging to {first_name} {last_name}' + 
					' has been added to the book.')
			else:
				print(f'There is already an email associated with {first_name} {last_name}.')

			self.get_controller().render_main_view()

	class LookUpAddressView(BaseView):

		def __init__(self, name, controller):
			super().__init__(name, controller)

		def render(self):
			print()
			print()
			print('Look up an existing address:')
			print()
			first_name, last_name = self.name_prompt()

			results = (self.get_controller()
				.look_up_email_address(first_name, last_name))

			print()
			if results:
				print(f'The email belonging to {first_name} {last_name} is {results[1]}.')
			else:
				print(f'There is no email associated with {first_name} {last_name}.')

			self.get_controller().render_main_view()

	class UpdateAddressView(BaseView):

		def __init__(self, name, controller):
			super().__init__(name, controller)

		def render(self):
			print()
			print()
			print('Update an existing email address:')
			print()
			first_name, last_name = self.name_prompt()
			email = self.email_prompt()
			
			results = (self.get_controller()
				.update_email_address(first_name, last_name, email))

			print()
			if results:
				print(f'The Email belonging to {first_name} {last_name}' + 
					' has been updated.')
			else:
				print(f'There is no email associated with {first_name} {last_name}.')

			self.get_controller().render_main_view()

	class DeleteAddressView(BaseView):

		def __init__(self, name, controller):
			super().__init__(name, controller)

		def render(self):
			print()
			print()
			print('Delete an email address:')
			print()
			first_name, last_name = self.name_prompt()

			results = (self.get_controller()
				.delete_email_address(first_name, last_name))

			print()
			if results:
				print(f'{first_name} {last_name} has been added removed from the book.')
			else:
				print(f'There is no email associated with {first_name} {last_name}.')

			self.get_controller().render_main_view()

	class ViewAllAddressesView(BaseView):

		def __init__(self, name, controller):
			super().__init__(name, controller)

		def render(self):
			print()
			print()
			print('Emails inside the address book:')
			print()

			results = self.get_controller().get_email_addresses()

			print()
			if len(results) > 0:
				print('{:<30} {:<30}'.format('Full Name', 'Email Address'))
				print()
				for full_name, email in results.items():
					print('{:<30} {:<30}'.format(full_name.replace('_', ' '), email))
			else:
				print('The email address book is empty.')

			self.get_controller().render_main_view()

	class Controller():

		def __init__(self, model):
			self.__model = model

			# Instantiate views
			self.__main_view = MainView(MAIN_VIEW, self)
			self.__create_address_view = CreateAddressView(CREATE_ADDRESS_VIEW, self)
			self.__lookup_address_view = LookUpAddressView(LOOKUP_ADDRESS_VIEW, self)
			self.__update_address_view = UpdateAddressView(UPDATE_ADDRESS_VIEW, self)
			self.__delete_address_view = DeleteAddressView(DELETE_ADDRESS_VIEW, self)
			self.__view_all_addresses_view = ViewAllAddressesView(View_ALL_ADDRESSES_VIEW, self)

			# Kickstart app by rendering main view
			self.__main_view.render()

		def on_receive_data_from_view(self, data):
			origin = data['origin']

			if origin == MAIN_VIEW:
				self.handle_data_from_main_view(data)

		def handle_data_from_main_view(self, data):
			event = data['event']
			payload = data['payload']

			if event == USER_CHOICE_EVENT:
				choice = payload['choice']

				if choice == 0:
					# Write to binary before exit
					self.__model.write()
				elif choice == 1:
					self.__create_address_view.render()
				elif choice == 2:
					self.__lookup_address_view.render()
				elif choice == 3:
					self.__update_address_view.render()
				elif choice == 4:
					self.__delete_address_view.render()
				elif choice == 5:
					self.__view_all_addresses_view.render()

		def create_email_address(self, first_name, last_name, email):
			return self.__model.create(first_name, last_name, email)

		def look_up_email_address(self, first_name, last_name):
			return self.__model.read(first_name, last_name)

		def update_email_address(self, first_name, last_name, email):
			return self.__model.update(first_name, last_name, email)

		def delete_email_address(self, first_name, last_name):
			return self.__model.delete(first_name, last_name)

		def get_email_addresses(self):
			return self.__model.get()

		def render_main_view(self):
			self.__main_view.render()

	controller = Controller(Model())

if __name__ == '__main__':
	main()