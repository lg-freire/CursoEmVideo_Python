def dec2any(dec,base_final):
    base_final = int(base_final)
    dec = int(dec)
    dic = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numero_final_temp = []
    numero_final = ''
    while True:
        temp_numero_final = dec%base_final
        numero_final_temp.append(temp_numero_final)
        if int(dec/base_final) == 0:
            break
        dec = int(dec/base_final)
    numero_final_temp.reverse()
    for i in numero_final_temp:
        numero_final += dic[i]
    return numero_final


# It's possible to remove the first two characters of a string by adding [2:] to it.
n = int(input('Input a number: '))
print('2 = binary; 8 = octo; 16 = hexadecimal')
base = int(input('Input the base: '))
if base == 2:
    bnr = dec2any(n, 2)
    print(f'Number in binary: {bnr}')
elif base == 8:
    octo = dec2any(n, 8)
    print(f'Number in octo: {octo}')
elif base == 16:
    hex = dec2any(n, 16)
    print(f'Number in hexadecimal: {hex}')
else:
    print('Invalid base.')
