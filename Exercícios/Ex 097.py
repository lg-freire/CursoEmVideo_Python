def write(st):
    print('~' * (len(st) + 4))
    print(f'  {st}  ')
    print('~' * (len(st) + 4))


for i in range(0, 2):
    phrase = input(f'Sentence #{i+1}: ')
    write(phrase)
