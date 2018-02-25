# Program 6-28
# Handles a ValueError exception.

def main():
	try:
		hours = int(input('How many hours did you work? '))

		pay_rate = float(input('Enter your hourly pay rate: '))

		gross_pay = hours * pay_rate

		print(f"Gross pay: ${format(gross_pay, ',.2f')}")
	except ValueError as err:
		print(err)

main()