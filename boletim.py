# aluno entra com notas

nome = input('Qual seu nome:\n')
nota = str(input('Qual sua nota:\n')).replace(',', '.')
nota = float(nota)

# verifica
if nota >= 7:
    print(f'{nota} Aprovado')
elif nota >= 5:
    print(f'{nome} está de recuperação')
else:
    print(f'{nome} está reprovado')

