# This program displays a label with text.

import tkinter

class MyGUI:

	def __init__(self):

		self.main_window = tkinter.Tk()

		# Creates a label widget containing the
		# text "Hello world!"
		self.label1 = tkinter.Label(self.main_window, text='Hello world!')
		self.label2 = tkinter.Label(self.main_window, text='This is a GUI program.')

		# Determines where a widget should be
		# positioned and makes the widget visible
		# when the window is displayed.
		self.label1.pack()
		self.label2.pack()
		
		tkinter.mainloop()

my_gui = MyGUI()