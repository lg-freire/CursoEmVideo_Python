from time import sleep
print('-' * 60)
print(f"{'SUPA FIGHTER STORE':^60}")
print(f"{'Da best of da best gear!!!':^60}")
print('-' * 60)
print('\033[34mLeave the name field empty to terminate the program.\033[m')
print('-' * 60)
total = exp = cheapv = 0
cheapn = None

while True:
    name = input('Product name: ').strip()
    if name == '':
        print('\033[33m EXIT CONDITION ACKNOWLEDGED.\033[m')
        break
    while True:
        try:
            price = float(input('Price: US$'))
            break
        except ValueError:
            print(f"""\033[31mINVALID INPUT.\033[m
Please insert a valid price.""")
    total += price
    if price >= 1000:
        exp += 1
    if cheapv == 0 or price < cheapv:
        cheapv = price
        cheapn = name
    

sleep(1.5)
print('-' * 18)
print("PROGRAM TERMINATED")
print(f"""Total value: US${total:.2f}
{exp} item(s) was/were above US$ 1000.00
The cheapest item was {cheapn} costing US${cheapv:.2f}""")
