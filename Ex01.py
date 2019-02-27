v = int(input('Qual o valor da casa?? R$'))
s = float(input('Quanto vc ganha?? '))
a = float(input('Em quantos anos vc quer financiar?? '))
p = (v / (a * 12))
if p > (s * 0.3):
    print(f'Para pagar uma casa de R${v} em {int(a)} anos a prestação será de R${p:.2f}. Empréstimo NEGADO!')
elif p <= (s * 0.3):
    print(f'Para pagar uma casa de R${v} em {int(a)} anos a prestação será de R${p:.2f}. Empréstimo CONCEDIDO!')
