d = float(input('Travel distance: '))
if d <= 200:
    print('Price: US${:.2f}'.format(d * 0.5))
else:
    print('Price: US${:.2f}'.format(d * 0.45))
