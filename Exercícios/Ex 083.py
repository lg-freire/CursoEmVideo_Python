exp = list(str(input('Input the equation: ')).strip())
if exp.count('(') == exp.count(')'):
    print('This is a valid equation.')
else:
    print('This is not a valid equation.')
