pesos = []
for i in range(0, 5):
    w = float(input(f'Weight of subject #{i+1}: '))
    pesos.append(w)

pesos.sort()
print(f'The heaviest subjects weighs\033[91m {pesos[-1]:.1f}\033[m kg and the lightest subject weighs'
      f'\033[94m {pesos[0]:.1f}\033[m kg.')
