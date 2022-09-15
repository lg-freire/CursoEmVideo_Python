dic = {'name': input('Student name: ')}
dic['median'] = float(input(f"{dic['name']}'s average: "))
print(f'Name: {dic["name"]}')
print(f'Average: {dic["median"]:.1f}')
if dic['median'] >= 7:
    print(f'{dic["name"]} is approved.')
else:
    print(f'{dic["name"]} is held back.')
