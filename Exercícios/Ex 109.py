from Modules import money

n = float(input('Price: US$'))
print(f'''Half of {money.money(n)} is {money.double(n, True)}
{money.money(n)} doubled is {money.double(n, True)}
A 20% increase on {money.money(n)} is {money.increase(n, 20, True)}
A 30% discount on {money.money(n)} is {money.discount(n, 30, True)}''')
