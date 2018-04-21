# This program converts distances in kilometers
# to miltes.  The result is displayed in an info
# dialog box.

import tkinter
import tkinter.messagebox

class MyGUI:

	def __init__(self):

		self.main_window = tkinter.Tk()

		self.top_frame = tkinter.Frame(self.main_window)
		self.mid_frame = tkinter.Frame(self.main_window)
		self.bottom_frame = tkinter.Frame(self.main_window)

		self.prompt_label = tkinter.Label(
			self.top_frame, \
			text='Enter a distance in kilometers:'
		)

		self.kilo_entry = tkinter.Entry(
			self.top_frame, \
			width=10
		)

		self.prompt_label.pack(side='left')
		self.kilo_entry.pack(side='left')

		self.descr_label = tkinter.Label(
			self.mid_frame, \
			text='Converted to miles:'
		)

		# We need a StringVar object to associate with
		# an output label. Use the object's set method
		# to store a string of blank characters.
		self.value = tkinter.StringVar()

		# Any value in self.value will be
		# displayed in this label
		self.miles_label = tkinter.Label(
			self.mid_frame, \
			textvariable=self.value
		)

		self.descr_label.pack(side='left')
		self.miles_label.pack(side='left')

		self.calc_button = tkinter.Button(
			self.bottom_frame, \
			text='Convert', \
			command=self.convert
		)

		self.quit_button = tkinter.Button(
			self.bottom_frame, \
			text='Quit', \
			command=self.main_window.destroy
		)

		self.calc_button.pack(side='left')
		self.quit_button.pack(side='left')

		# Pack the frames.
		self.top_frame.pack()
		self.mid_frame.pack()
		self.bottom_frame.pack()

		tkinter.mainloop()

	def convert(self):
		# Get the value entered by the user into
		# the kilo_entry widget.
		kilo = float(self.kilo_entry.get())

		miles = kilo * 0.6214

		self.value.set(miles)

my_gui = MyGUI()

