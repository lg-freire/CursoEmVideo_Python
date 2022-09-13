print(f'\033[31m{"STUPID EXERCISE IN WHICH WE PRETEND THE SORT COMMAND DOES NOT EXIST"}\033[m')
print('-=-' * 23)
nums = []

for i in range(0, 5):
    n = int(input(f'Input number #{i+1}: '))
    if not nums:
        nums.append(n)
        print(f'Added number {n} to the list.')
    else:
        if min(nums) >= n:
            nums.insert(0, n)
            print(f'Number {n} inserted in the position #{nums.index(n)} of the list.')
        elif n >= max(nums):
            nums.append(n)
            print(f'Number {n} inserted at the end of the list.')
        else:
            for x in range(0, len(nums)):
                if n <= nums[x]:
                    nums.insert(x, n)
                    print(f'Number {n} inserted in the position #{nums.index(n)} of the list.')
                    break

print(nums)
