from math import pow, sqrt
side1 = float(input('Adjacent side: '))
side2 = float(input('Opposite side: '))
hyp = sqrt(pow(side1, 2) + pow(side2, 2))
print('Hypotenuse: {:.2f}'.format(hyp))
