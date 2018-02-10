# Program 5-15

CONTRIBUTION_RATE = 0.05 # global constant

def main():
	gross_pay = float(input('Enter gross pay: '))
	bonus = float(input('Enter bonus: '))
	show_pay_contrib(gross_pay)
	show_bonus_contrib(bonus)

def show_pay_contrib(gross):
	contrib = gross * CONTRIBUTION_RATE
	print('Contribution for gross pay:  $', \
		format(contrib, ',.2f'), \
		sep='')

def show_bonus_contrib(bonus):
	contrib = bonus * CONTRIBUTION_RATE
	print('Contribution for bonuses: $', \
		format(contrib, ',.2f'), \
		sep='')

main()