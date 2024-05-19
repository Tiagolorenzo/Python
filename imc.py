# dados: Menor que 18,5 = Baixo peso, 18,5 a 24,9 = Peso normal, 25 a 29,9 = Sobrepeso, 30 a 34,9 =	Obesidade grau I, 35 a 39.9	= Obesidade grau II, Igual ou maior que 40	Obesidade grau III.

# entrada de dados:
try:
    peso = int(input('Diga seu peso:\n'))
    altura = str(input('Diga sua altura:\n')).replace(',', '.')

    altura = float(altura)

    if altura <= 0 or peso <= 0:
        print("Altura e peso devem ser valores positivos.")

    else:
        imc = peso / (altura ** 2)
        print(f'Seu IMC é: {imc:,.2f}')

    if imc < 18.5:
        print('Abaixo do peso')
    elif 18.5 <= imc < 24.9:
        print('Peso normal')
    elif 25 <= imc < 29.9:
        print('Sobrepeso')
    else:
        print('Obesidade')

except:
    print('insira valores válidos.')



