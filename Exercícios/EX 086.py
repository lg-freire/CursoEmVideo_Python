nums = []

for i in range(0, 3):
    for j in range(0, 3):
        nums.append(int(input(f'Value for [{i}, {j}]: ')))

for f, i in enumerate(nums):
    print(f'[{i:^6}]', end='')
    if (f + 1) % 3 == 0:
        print()
