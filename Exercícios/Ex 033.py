n1 = float(input('First number: '))
n2 = float(input('Second number: '))
n3 = float(input('Third number: '))
if n1 > n2:
    if n1 > n3:
        if n2 > n3:
            print('{} is the biggest number, {} is the smallest number.'.format(n1, n3))
        else:
            print('{} is the biggest number, {} is the smallest number.'.format(n1, n2))
    else:
        print('{} is the biggest number, {} is the smallest number.'.format(n3, n2))
elif n3 > n2:
    if n1 > n3:
        print('{} is the biggest number, {} is the smallest number.'.format(n1, n2))
    else:
        print('{} is the biggest number, {} is the smallest number.'.format(n3, n1))
else:
    if n1 > n3:
        print('{} is the biggest number, {} is the smallest number.'.format(n2, n3))
    else:
        print('{} is the biggest number, {} is the smallest number.'.format(n2, n1))
