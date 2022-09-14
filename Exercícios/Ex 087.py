nums = []
s = cs = m = 0

for i in range(0, 3):
    for j in range(0, 3):
        nums.append(int(input(f'Value for [{i}, {j}]: ')))

for f, i in enumerate(nums):
    print(f'[{i:^7}]', end='')
    if (f + 1) % 3 == 0:
        print()

for n in nums:
    if n % 2 == 0:
        s += n
print(f'The sum of all even numbers is {s}.')

for n in nums:
    if n % 3 == 0:
        cs += n
print(f'The sum of all numbers in the third row is {cs}.')

for i in range(3, 6):
    if nums[i] > m:
        m = nums[i]
print(f'The highest number in the second line is {m}.')
