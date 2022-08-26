num = input('Input a number from 0 to 9999: ')
while len(num) > 4:
    num = input('Input a number from 0 to 9999: ')

print("""
Unit: {}
Ten: {}
Hundred: {}
Thousand {}""".format(num[3], num[2], num[1], num[0]))
