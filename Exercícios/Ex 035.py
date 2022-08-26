l1 = float(input('Side #1: '))
l2 = float(input('Side #2: '))
l3 = float(input('Side #3: '))
if l1 + l2 > l3:
    if l1 + l3 > l2:
        if l2 + l3 > l1:
            print('This is a valid triangle.')
else:
    print('This is not a valid triangle.')
