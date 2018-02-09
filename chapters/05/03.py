# Program 5-3
# This program displays step-by-step instructions
# for disassembling an Acme dryer.

# The main function performs the program's main logic.
def main():
	startup_message()
	
	input('Press Enter to see Step 1.')
	step1()

	input('Press Enter to see Step 2.')
	step2()

	input('Press Enter to see Step 3.')
	step3()

	input('Press Enter to see Step 4.')
	step4()

def startup_message():
	print('This program tells you how to')
	print('disassemble an ACME laundry dryer.')
	print('There are 4 steps in the process.')
	print()

def step1():
	print('Step 1: Unplug the dryer and move it away from the wall.')
	print()

def step2():
	print('Step 2: Remove the six screws from the back of the dryer.')
	print()

def step3():
	print('Step 3: Remove the back panel.')
	print()

def step4():
	print('Step 4: Pull the top of the dryer straight up.')
	print()

main()