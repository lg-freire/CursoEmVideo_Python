house = float(input('Price of house: US$'))
wage = float(input('Salary of buyer: US$'))
years = int(input('Number of years:'))
part = house / (years * 12)
if part <= (wage * 0.3):
    print('Monthly payments of US${:.2f}'.format(part))
else:
    print('Loan denied')
