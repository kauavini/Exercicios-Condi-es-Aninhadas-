peso = float(input('Qual o seu peso? (Kg)'))
alt = float(input('Qual a sua altura? '))
imc = peso / (alt * alt)
print(f'O seu IMC é {imc:.1f}')
if imc < 18.5:
    print('Você está ABAIXO DO PESO.')
elif imc >= 18.5 and imc < 25:
    print('Você está no PESO IDEAL.')
elif imc >= 25 and imc < 30:
    print('Você está na faixa do SOBREPESO.')
elif imc >= 30 and imc < 40:
    print('Você está em OBESIDADE.')
else:
    print('Você está em OBESIDADE MÓRBIDA.')

