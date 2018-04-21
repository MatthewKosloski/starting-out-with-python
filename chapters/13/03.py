# This program displays a label with text.

import tkinter

class MyGUI:

	def __init__(self):

		self.main_window = tkinter.Tk()

		# Creates a label widget containing the
		# text "Hello world!"
		self.label = tkinter.Label(self.main_window, text='Hello world!')

		# Determines where a widget should be
		# positioned and makes the widget visible
		# when the window is displayed.
		self.label.pack()
		
		tkinter.mainloop()

my_gui = MyGUI()