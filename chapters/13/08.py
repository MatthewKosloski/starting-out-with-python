# This program demonstrates a Quit button.

import tkinter
import tkinter.messagebox

class MyGUI:

	def __init__(self):

		self.main_window = tkinter.Tk()

		self.my_button = tkinter.Button(
			self.main_window, \
			text='Click me!', \
			command=self.do_something
		)

		self.quit_button = tkinter.Button(
			self.main_window, \
			text = 'Quit', \
			command=self.main_window.destroy
		)

		self.my_button.pack()
		self.quit_button.pack()

		tkinter.mainloop()

	def do_something(self):
		print('Doing something...')
		tkinter.messagebox.showinfo(
			'Response', \
			'Thanks for clicking the button!' \
		)

my_gui = MyGUI()

