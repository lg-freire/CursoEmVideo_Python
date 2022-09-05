p = str(input('Write a phrase to check for palindrome: ')).strip().upper().split()
p = ''.join(p)
if p == p[::-1]:
    print("It's a palindrome.")
else:
    print('Not a palindrome.')
