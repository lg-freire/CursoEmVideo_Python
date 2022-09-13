print('\033[34mGIVE ME FOUR NUMBERS FOR ANALYSIS\033[m')
print('-+-' * 12)
t = ev = ()
for i in range(0, 4):
    while True:
        try:
            ent = int(input(f'#{i+1}: '))
            t += (ent,)
            break
        except ValueError:
            print('\033[31mPlease input a number.\033[m')
print(f"The number 9 was given {t.count(9)} times.")
if 3 in t:
    print(f'The first number 3 was the #{t.index(3)+1} entrance.')
else:
    print('You did not give me the number 3.')
for i in t:
    if i % 2 == 0:
        ev += i,
if ev != ():
    print(f'The even numbers you gave me were {ev}.')
else:
    print('You did not give me any even numbers.')
