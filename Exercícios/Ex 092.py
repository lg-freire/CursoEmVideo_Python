from datetime import datetime
people = {'name': input('Name of subject: '), 'birth': int(input('Birth year: ')), 'work': int(input('Work registry '
                                                                                                     '(0 for none): '))}
if people['work'] != 0:
    people['year'] = int(input('Hired in: '))
    people['wage'] = int(input('Salary: US$'))

age = datetime.today().year - people['birth']
ret = age + (35 - (datetime.today().year - people['year']))

print(f"""Subject name: {people['name']}
Subject age: {age}""")
if people['work'] == 0:
    print('Subject has never worked.')
else:
    print(f"""Subject work registry: {people['work']}
Subject was hired in {people['year']}
Subject currently has a salary of US${people['wage']:.2f}
Subject may retire by {ret} years old""")
