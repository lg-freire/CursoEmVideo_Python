pesos = []
for i in range(0, 2):
    w = float(input(f'Weight of subject #{i+1}: '))
    pesos.append(w)

pesos.sort()
print(f'The heaviest subjects weighs {pesos[-1]:.1f}kg and the lightest subject weighs {pesos[0]:.1f}kg.')
