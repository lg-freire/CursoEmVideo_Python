h = float(input('Height (in m): '))
w = float(input('Weight (in kg): '))
imc = w / (pow(h, 2))
if imc <= 18.5:
    print('Lanklet.')
elif 18.5 < imc <= 25:
    print('DYEL')
elif 25 <= imc < 30:
    print('Big boi.')
elif 30 <= imc < 40:
    print('Lard.')
else:
    print('Nikocado Avocado.')
