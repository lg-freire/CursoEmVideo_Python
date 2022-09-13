li = ('Dildo', 6.66, 'Jabroni Outfit', 82.99, 'Gym Membership', 39.99)
print('-' * 39)
print(f'{"PRICE LISTING":^39}')
print('-' * 39)

for i in range(0, len(li), 2):
    print(f"{li[i]:.<30}US${li[i+1]:6}")

print('-' * 39)
