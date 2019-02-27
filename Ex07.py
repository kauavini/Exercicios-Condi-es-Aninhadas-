l1 = int(input('Primeiro segmento: '))
l2 = int(input('Segundo segmentp: '))
l3 = int(input('Terceiro segmento: '))
if l1 < (l2 + l3) and l2 < (l1 + l3) and l3 < (l1 + l2):
    tipo = ''
    if l1 == l2 and l1 == l3:
        tipo = 'Equilátero'
    elif l1 != l2 and l1 != l3:
        tipo = 'Escaleno'
    else:
        tipo = 'Isósceles'
    print(f'Os segmentos PODEM FORMAR um triângulo {tipo}.')
else:
    print('Os segmentos NÃO PODEM formar um triângulo.')

