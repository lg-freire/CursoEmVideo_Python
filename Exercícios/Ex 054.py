from datetime import date

now = date.today().year
a = 0
u = 0
for i in range(0, 7):
    b = int(input(f'Birth year of subject #{i+1}: '))
    age = now - b
    if age >= 18:
        a += 1
    elif age < 18:
        u += 1
print(f'{a} subjects are of age and {u} subjects are underage.')
