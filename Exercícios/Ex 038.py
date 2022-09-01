n1, n2 = map(int, input('Type two numbers to be compared: ').split())
if n1 > n2:
    print('The first number is bigger.')
elif n1 < n2:
    print('The second number is bigger.')
elif n1 == n2:
    print("They're the same number.")
