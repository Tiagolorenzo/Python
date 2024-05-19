# qual filme está passando em qual sala. o cinema em questão tem 5 salas. Se eu selecionar um número dentro do número de salas existentes, o programa deverá me retornar o nome do filme que está passando na sala escolhida.

nome = input('Qual seu nome:\n')

# exibe a lista de filmes e suas salas
print('LISTA DE FILMES\n')
print('Sala 1 - A volta dos que não foram')
print('Sala 2 - As tranças do careca')
print('Sala 3 - O mar vai pegar fogo')
print('Sala 4 - Poeira em alto mar')
print('Sala 5 - Em terra de cegos quem tem um olho é Rei')

# recebe sala escolhida
sala = int(input('Informe sala desejada:\n'))

match sala:
    case 1:
        print(f'Filme escolhido por {nome}: A volta dos que não foram')
    case 2:
        print(f'Filme escolhido por {nome}: As tranças do careca')
    case 3:
        print(f'Filme escolhido por {nome}: O mar vai pegar fogo')
    case 4:
        print(f'Filme escolhido por {nome}: Poeira em alto mar')
    case 5:
        print(f'Filme escolhido por {nome}: Em terra de cegos quem tem um olho é Rei')
    case _:
        print('Sala inesistente!!!')
        
