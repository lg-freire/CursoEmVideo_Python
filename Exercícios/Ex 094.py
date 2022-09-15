from time import sleep

people = []
total = 0
count = 1

while True:
    person = {'name': input(f'Name of subject #{count}: '), 'sex': input(f'Gender of subject #{count} [M/F]: '),
              'age': int(input(f'Age of subject #{count}: '))}
    people.append(person)
    total += person['age']
    count += 1
    flag = input('Continue [Y/N]: ').strip().lower()
    while flag not in 'yn':
        flag = input("""\033[31mINVALID INPUT\033[m
Continue [Y/N]: """).strip().lower()
    if flag == 'n':
        print("\033[32mTERMINATING PROGRAM...\033[m")
        break

median = total / len(people)

print('-=' * 25)
sleep(1.5)

print(f"""This group consists of {len(people)} subjects.
The average age of the group is {median}.
\033[36mThe female subjects were:\033m""")
for i in people:
    if i['sex'] in 'Ff':
        print(f'=> {i["name"]}', end=' ')
print('\n\033[34mSubjects over the average age:\033[m ')
for i in people:
    if i['age'] > median:
        print(f"Subject: {i['name']}; Sex: {i['sex']}; Age: {i['age']}")
