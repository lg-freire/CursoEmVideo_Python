p = float(input('Original price: US$ '))
print('0 = cash; 1 = credit; 2 = credit (2 installments); 3 = credit (3 or more)')
c = int(input('Payment in: '))
if c == 0:
    print('Final price: US${:.2f}'.format(p * 0.9))
elif c == 1:
    print('Final price: US${:.2f}'.format(p * 0.95))
elif c == 2:
    print('Final price: US${:.2f}'.format(p))
elif c == 3:
    print('Final price: US${:.2f}'.format(p * 1.2))
