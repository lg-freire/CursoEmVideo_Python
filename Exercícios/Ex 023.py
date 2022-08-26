num = int(input('Input a number from 0 to 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print("""Unit: {}
Ten: {}
Hundred: {}
Thousand {}""".format(u, d, c, m))
