from random import shuffle
group1 = input('Group #1: ')
group2 = input('Group #2: ')
group3 = input('Group #3: ')
group4 = input('Group #4: ')
groups = [group1, group2, group3, group4]
shuffle(groups)
print(groups)
