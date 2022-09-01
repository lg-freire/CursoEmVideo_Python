l1, l2, l3 = map(float, input('Input the sides of the triangle: ').split())
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    if l1 == l2 == l3:
        print('Equilateral triangle.')
    elif l1 == l2 != l3 or l1 == l3 != l2 or l2 == l3 != l2:
        print('Isosceles triangle.')
    elif l1 != l2 != l3:
        print('Scalene triangle.')
else:
    print('Not a triangle.')
