print('vamos calcular o seu IMC para saber se você está em forma?')
vezes = int(input('quantas vezes pretende fazer esse calculo?'))
for x in range(vezes):
    peso = float(input('Quanto você pesa? '))
    altura = float(input('Qual é a sua altura? '))
    imc = peso/(altura*altura)
    print(imc)


