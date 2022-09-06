n = int(input("Input the number of digits of the Fibonacci sequence you'd like to see: "))
print('0', end=' > ')
f, fm, fm2 = 1, 1, 0
while n != 0:
    if n > 1:
        print(f, end=' > ')
    else:
        print(f, end='')
    f = fm + fm2
    fm2 = fm
    fm = f
    n -= 1
