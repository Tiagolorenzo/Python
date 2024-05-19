# Usuário entra com nome, altura e idade.

nome = input('Qual seu nome:\n')
idade = int(input('Informe sua idade:\n'))
altura = str(input('Informe sua altura:\n')).replace(',', '.')
# Converte altura para float
altura = float(altura)

# Verifica as condições
if idade >= 12 and altura >= 1.2:
    print(f'{nome} Pode entrar!')
else:
    print(f'{nome} Cresça!!!')
    