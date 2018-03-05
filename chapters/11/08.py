# Program 11-8
# Creates an instance of SavingsAccount
# class and an instance of the CD account.

import accounts

def main():

	print('Enter the following data for a savings account.')
	acct_num = input('Account number: ')
	int_rate = float(input('Interest rate: '))
	balance = float(input('Balance: '))

	savings = accounts.SavingsAccount(acct_num, int_rate, balance)

	print('Enter the following info for a CD:')
	acct_num = input('Account number: ')
	int_rate = float(input('Interest rate: '))
	balance = float(input('Balance: '))
	maturity = input('Maturity date:')

	cd = accounts.CD(acct_num, int_rate, balance, maturity)

	print('Here is the data you entered:')

	print()

	print('Savings Account')
	print('---------------')
	print('Account number:', savings.get_account_num())
	print('Interest rate:', savings.get_interest_rate())
	print('Balance: $', format(savings.get_balance(), ',.2f'), sep='')

	print()

	print('CD')
	print('---------------')
	print('Account number:', cd.get_account_num())
	print('Interest rate:', cd.get_interest_rate())
	print('Balance: $', format(cd.get_balance(), ',.2f'), sep='')
	print('Maturity date:', cd.get_maturity_date())

main()