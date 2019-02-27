num = int(input('Digite um valor: '))
print('''[1]BINÁRIA
[2]OCTAL
[3]HEXADECIMAL''')
b = int(input('Para qual base vc quer converter? '))
if b == 1:
    print(f'O número {num} convertido para a base binária é {bin(num)}')
elif b == 2:
    print(f'O número {num} convertido para a base octal é {oct(num)}')
elif b == 3:
    print(f'O número {num} convertido para a base hexadecimal é {hex(num)}')