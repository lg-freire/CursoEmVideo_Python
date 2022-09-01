import datetime
birth = int(input('Birth year: '))
date = datetime.date.today()
year = int(date.strftime('%Y'))
age = year - birth
if age < 18:
    print("You're safe.")
elif age == 18:
    print('Go ye hero, go and die.')
else:
    print('Go to jail.')
