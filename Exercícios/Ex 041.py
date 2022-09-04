from datetime import date
birth = int(input('Year of birth: '))
now = date.today().year
age = now - birth
if age <= 9:
    print('MIRIM')
elif 9 < age <= 14:
    print('INFANTIL')
elif 14 < age <= 19:
    print('JUNIOR')
elif 19 < age <= 20:
    print('SENIOR')
else:
    print('MASTER')
