from datetime import date
birth = int(input('Birth year: '))
now = date.today().year
age = now - birth
if age < 18:
    print("You're safe.")
elif age == 18:
    print('Go ye hero, go and die.')
else:
    print('Go to jail.')
