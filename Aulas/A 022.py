def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f


num = int(input('Dgite um valor: '))
fat = factorial(num)
print(f'O fatorial de {num} é {fat}.')
