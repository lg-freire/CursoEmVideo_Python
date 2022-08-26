wage = float(input('Current wage (in USD): '))
if wage >= 1250.0:
    print('New wage: US$ {:.2f}'.format(wage * 1.1))
else:
    print('New wage: USD {:.2f}'.format(wage * 1.15))
