n1 = float(input('Digite sua primeira nota:  '))
n2 = float(input('Digite sua segunda nota: '))
print(f'Quem tirou notas {n1} e {n2} tem média {(n1 + n2)/2}')
if ((n1 + n2)/2) < 5:
    print('O aluno está REPROVADO.')
elif ((n1 + n2) / 2) >= 7:
    print('O alun está APROVADO.')
else:
    print('O aluno está de RECUPERÇÃO.')