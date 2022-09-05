old = ''
w = 0
ages, mage, names = [], [], []
for i in range(0, 1):
    name = str(input(f'Name of subject #{i+1}: ')).strip()
    age = int(input(f'Age of subject #{i+1}: '))
    gend = str(input(f"""Subject #{i+1} is:
[ M ] Male
[ F ] Female
""")).strip().lower()
    ages.append(age)
    if gend == 'm':
        mage.append(age)
        names.append(name)
    if gend == 'f' and age <= 20:
        w += 1

soma = 0
for sumAge in ages:
    soma += sumAge
median = soma / 4

old = max(mage)
ind = mage.index(old)
oldname = names[ind]

print(f"This group's median age is {median}. The oldest male subject is {oldname} at {old} years old. There are {w} "
      f"female subjects under 20 years of age.")
