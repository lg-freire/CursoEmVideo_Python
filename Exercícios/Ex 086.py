nums = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0, 3):
    for j in range(0, 3):
        nums[i][j] = int(input(f'Value for [{i}, {j}]: '))

print('-=' * 20)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{nums[i][j]:^6}]', end='')
    print()
