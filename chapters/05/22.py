# Program 5-22
# Calculates a retual item's
# sale price.

DISCOUNT_PERCENTAGE = 0.20

def main():
	reg_price = get_regular_price()

	sales_price = reg_price - discount(reg_price)

	print('The sale price is $', format(sales_price, ',.2f'), sep='')

def get_regular_price():
	price = float(input('Enter the item\'s regular price: '))
	return price

def discount(price):
	return price * DISCOUNT_PERCENTAGE

main()