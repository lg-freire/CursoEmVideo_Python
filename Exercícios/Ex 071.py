print('=' * 60)
print(f"{'Foundation for American Growth':^60}")
print('=' * 60)
value = int(input('\033[34mHow much would you like to withdraw today?\033[m\nUS$'))
bill = 50
nbill = 0
print('=' * 60)
print("That'll be:")

while True:
    if value >= bill:
        value -= bill
        nbill += 1
    else:
        if nbill > 0:
            print(f'{nbill} ${bill} bill(s)')
        if bill == 50:
            bill = 20
        elif bill == 20:
            bill = 10
        elif bill == 10:
            bill = 1
        nbill = 0
        if value == 0:
            break

print("\033[31mGoodbye.\033[m")
