print('-=-=-=-LOJA DO EDGAR-=-=-=-=')
valor = float(input('Qual o valor da sua compra? R$'))
print('''[1]à vista no dinheiro /cheque
[2]à vista no cartão
[3]2x no cartão
[4]3x ou mais no cartão''')
op = int(input('Qual a sua opção? '))
if op == 1:
    print(f'Com o pagamento à vista, sua compra de R${valor} vai ficar por R${valor - (valor * 0.1)}')
elif op == 2:
    print(f'Com o pagamento à vista no cartão, sua compra de {valor} vai ficar por R${valor - (valor * 0.05)}')
elif op == 3:
    print(f'Com o pagamento em 2x no cartão, sua compra não vai ter nenhum desconto ou juros, ficará com o preço normal.')
elif op == 4:
    v = int(input('Em quantas vezes quer dividir?'))
    print(f'Com o pagamento em {v}x no cartão, as suas prestações serão de R${(valor + (valor * 0.2))/v}, pois terá um aumento de 20%. A sua compra de {valor} ficará por {valor + (valor*0.2)}')