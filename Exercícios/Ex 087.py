nums = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
s = cs = m = 0

for i in range(0, 3):
    for j in range(0, 3):
        nums[i][j] = (int(input(f'Value for [{i}, {j}]: ')))

for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{nums[i][j]:^6}]', end='')
        if nums[i][j] % 2 == 0:
            s += nums[i][j]
    print()

print(f'The sum of all even numbers is {s}.')

for n in range(0, 3):
    cs += nums[n][2]
print(f'The sum of all numbers in the third row is {cs}.')

m = max(nums[1])
print(f'The highest number in the second line is {m}.')
