from random import randint
dice = {}
for i in range(0, 4):
    dice[f'Player {i+1}'] = randint(1, 6)

for k, v in dice.items():
    print(f'{k} played {v}.')
print('-=' * 15)
s = sorted(dice.items(), key=lambda x: x[1])
for c, i in enumerate(s):
    print(f'#{c+1}: {i[0]} with a roll of {i[1]}')
