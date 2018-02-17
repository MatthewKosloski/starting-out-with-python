# Program 10-5
# This program demonstrates the BankAccount class.

import bankaccount

def main():

	# Get the starting balance.
	start_bal = float(input('Enter your starting balance: '))

	# Create a BankAccount object
	savings = bankaccount.BankAccount(start_bal)

	# Deposit paycheck
	pay = float(input('How much were you paid this week? '))
	print('I will deposit that amount into your account.')
	savings.deposit(pay)

	# Display balance after deposit
	print('Your account balance is $', 
		format(savings.get_balance(), ',.2f'),
		sep='')

	# Get the amount to withdraw.
	cash = float(input('How much would you like to withdraw? '))
	print('I will withdraw that from your account.')
	savings.withdraw(cash)

	# Display balance after withdraw
	print('Your account balance is $', 
		format(savings.get_balance(), ',.2f'),
		sep='')

main()