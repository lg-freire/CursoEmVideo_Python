print(f'{"NUMBERED LIST ANALYZER":^30}')
print('-' * 30)
nums = maxnums = minnums = []

for c, i in enumerate(range(0, 5)):
    nums.append(input(f'Insert number #{c+1}: '))
print('-' * 30)
print(f'''Numbers inserted: {nums}
Highest inserted value: {max(nums)} in position(s): ''', end='')
for f, n in enumerate(nums):
    if n == max(nums):
        print(f'{f+1}..', end='')
print(f'\nLowest inserted number: {min(nums)} in position(s): ', end='')
for f, n in enumerate(nums):
    if n == min(nums):
        print(f'{f+1}..', end='')
