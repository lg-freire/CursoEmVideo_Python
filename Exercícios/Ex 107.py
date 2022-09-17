from Modules import money

n = float(input('Price: US$'))
print(f'''Half of {n} is {money.half(n)}
{n} doubled is {money.double(n)}
A 10% increase on {n} is {money.increase(n, 10)}
A 13% discount on {n} is {money.discount(n, 13)}''')
