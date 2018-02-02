# Program 4-14
# Displays gross pay.

# Get hours worked
hours = int(input('Enter hours worked this week: '))

# Get hourly pay rate
pay_rate = float(input('Enter pay rate: '))

# Calculate gross pay
gross_pay = hours * pay_rate

# Display gross pay
print('Gross pay: $', format(gross_pay, ',.2f'), sep='')