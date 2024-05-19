# Maior idade: programa vai receber nome e idade do usuário, se o usuário for maior de dezoito ira retornar você é maior de idade e o contrario menor de idade.

# entrada de dados:
nome = input('Informe seu nome:\n')
idade = int(input('informe sua idade:\n'))

# interpretação:
if idade >= 18:
    print(f'{nome} Voce é corôa!')
else:
    print(f'{nome} é novinho!')

