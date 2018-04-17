import pickle
import os.path

class EmailAddressBook():


	def __init__(self, file_name):
		self.__file_name = file_name

		self.__book = {}

		# Read from binary if it exists
		if self.file_exists():
			self.read_binary()

	'''
		Adds a new email to the book dictionary,
		where the key is the firstname and lastname
		separated by an underscore and the value is
		the email address. If the key exists, return
		an error string, else, add the email to the 
		dictionary and return the new entry as a tuple.

		@param first_name {str} First name of person
		@param last_name {str} Last name of person
		@return {tuple|str}
	'''
	def create(self, first_name, last_name, email):
		key = f'{first_name}_{last_name}'

		if not key in self.__book:
			self.__book[key] = email
			return (key, self.__book[key])
		else:
			return False

	'''
		Tries to get the email that is associated
		with the key: {first_name}_{last_name}. If
		the key exists, return the entry as a tuple.
		If the key does not exist and an exception
		is raised, return an error string.

		@param first_name {str} First name of person
		@param last_name {str} Last name of person
		@return {tuple|str}
	'''
	def read(self, first_name, last_name):
		key = f'{first_name}_{last_name}'

		try:
			return (key, self.__book[key])
		except KeyError:
			return False

	'''
		Update the email associated with the key:
		{first_name}_{last_} and return the updated
		entry as a tuple.

		@param first_name {str} First name of person
		@param last_name {str} Last name of person
		@return {tuple}
	'''
	def update(self, first_name, last_name, email):
		key = f'{first_name}_{last_name}'
		if key in self.__book:
			self.__book[key] = email
			return (key, self.__book[key])
		else:
			return False

	'''
		Deletes the email associated with the
		first name and last name. If there
		is no email associated with the name,
		return an error string.

		@param first_name {str} First name of person
		@param last_name {str} Last name of person
		@return {tuple}
	'''
	def delete(self, first_name, last_name):
		key = f'{first_name}_{last_name}'

		try:
			del self.__book[key]
			return True
		except KeyError:
			return False


	'''
		Returns the contents of the email address book.
	'''
	def get_book(self):
		return self.__book

	'''
		Tries to read from binary file and save data
		to self.__book. Raises exceptions if the file 
		doesn't exist or an error occurs while reading 
		from the file.
	'''
	def read_binary(self):
		try:
			with open(self.__file_name, 'rb') as input_file:
				self.__book = pickle.load(input_file)
		except FileNotFoundError:
			print(f'{self.__file_name} does not exist.')
		except IOError:
			print(f'An error occurred while trying to read from {self.__file_name}')

	'''
		Tries to save self.__book to a binary file. Rases 
		an exception if it is unable to write to the file.
	'''
	def write_binary(self):
		try:
			with open(self.__file_name, 'wb') as output_file:
				pickle.dump(self.__book, output_file)
		except IOError:
			print(f'An error occurred while trying to write to {self.__file_name}')

	'''
		Returns a boolean indicating if self.__file_name
		exits within the directory.

		@return {bool}
	'''
	def file_exists(self):
		return os.path.isfile(self.__file_name)
		