# This program displays an empty window.

import tkinter

class MyGUI:

	def __init__(self):
		# Create the main window widget.
		self.main_window = tkinter.Tk()

		# Enter the tkinter main loop.
		tkinter.mainloop()

my_gui = MyGUI()