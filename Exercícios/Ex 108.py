from Modules import money

n = float(input('Price: US$'))
print(f"""Half of {money.money(n)} is {money.money(money.half(n))}
{money.money(n)} doubled is {money.money(money.double(n))}
A 10% increase on {money.money(n)} is {money.money(money.increase(n, 10))}
A 13% discount on {money.money(n)} is {money.money(money.discount(n, 13))}""")
