# Program 10-6
# This program demonstrates the BankAccount class.

import bankaccount2

def main():

	# Get the starting balance.
	start_bal = float(input('Enter your starting balance: '))

	# Create a BankAccount object
	savings = bankaccount2.BankAccount(start_bal)

	# Deposit paycheck
	pay = float(input('How much were you paid this week? '))
	print('I will deposit that amount into your account.')
	savings.deposit(pay)

	# Display balance after deposit
	print(savings)

	# Get the amount to withdraw.
	cash = float(input('How much would you like to withdraw? '))
	print('I will withdraw that from your account.')
	savings.withdraw(cash)

	# Display balance after withdraw
	print(savings)

main()