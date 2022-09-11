print('=' * 60)
print(f"{'Foundation for American Growth'}:^60")
print('=' * 60)
value = int(input('\033[34mHow much would you like to withdraw today?\033[m\nUS$'))
n50 = n20 = n10 = n1 = 0

while True:
    if value >= 50:
        n50 = value // 50
        value -= n50 * 50
    if value >= 20:
        n20 = value // 20
        value -= n20 * 20
    if value >= 10:
        n10 = value // 10
        value -= n10 * 10
    n1 = value
    value -= n1
    if value == 0:
        break

print('=' * 60)
print(f"""That'll be:
{n50} $50 bills
{n20} $20 bills
{n10} $10 bills
{n1} $1 bills
\033[31mGoodbye.\033[m""")
