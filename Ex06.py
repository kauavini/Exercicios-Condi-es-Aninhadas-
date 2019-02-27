a = int(input('Ano de nascimento: '))
print(f'O atleta tem {2019 - a} anos.')
idade = 2019 - a
if idade <= 9:
    print('Classificação: Mirim')
elif idade <= 14:
    print('Classificação: Infantil')
elif idade <= 19:
    print('Classificação: Junior ')
elif idade <= 25:
    print('Classificação: Sênior')
else:
    print('Classificação: Master')