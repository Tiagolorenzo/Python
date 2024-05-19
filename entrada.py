# Crie um arquivo .py e faça um algoritmo que receba do usuário o nome, idade e profissão, e imprima na tela essas informações.
# .replace converte virgula pra ponto.
# Converte string para float


nome = input('Diga seu nome:')
idade = input('Diga sua idade:')
altura = str(input('Diga sua altura:')).replace(',', '.') 
altura = float(altura) 
profissao = input('Com que trabalha:')

print(f'Seu nome é {nome}, com idade de {idade} anos, altura {altura} metros de altura, e trabalha com {profissao}.')