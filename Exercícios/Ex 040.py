p1, p2 = map(float, input('Grades: ').split())
median = (p1 + p2) / 2
if median >= 7:
    print('Approved.')
elif 5 <= median < 7:
    print('Recuperation.')
elif median < 5:
    print('Held back.')
