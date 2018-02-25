# Program 6-22
# Calculate gross pay.

def main():
	hours = int(input('How many hours did you work? '))

	pay_rate = float(input('Enter your hourly pay rate: '))

	gross_pay = hours * pay_rate

	print(f"Gross pay: ${format(gross_pay, ',.2f')}")

main()