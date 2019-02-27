n = int(input('Ano de nascimento: '))
idade = 2019 - n
if idade < 18:
    print(f'Quem nasceu em {n} tem {idade} anos em 2019.')
    print(f'Ainda faltam {18 - idade} anos para o alistamento.')
    print(f'Seu alistamento será em {2019 + (18 - idade)}.')
elif idade > 18:
    print(f'Quem nasceu em {n} tem {idade} anos em 2019.')
    print(f'Você deveria ter se alistado há {idade - 18} anos.')
    print(f'Seu alistamento foi em {2019 - (idade - 18)}')
else:
    print(f'Quem nasceu em {n} tem 18 anos em 2019.')
    print('Você tem que se alistar imediatamente.')