print('vamos calcular o seu IMC para saber se você está em forma?')
vezes = int(input('quantas vezes pretende fazer esse calculo?'))
for x in range(vezes):
    peso = float(input('Quanto você pesa (em kilos)? '))
    altura = float(input('Qual é a sua altura (em metros)? '))
    alturax2 = altura*altura
    imc = peso/alturax2
    if imc < 18.5:
        print(imc, 'está muito baixo, considerado Magro')
    elif imc >= 18.5 and imc < 24.9:
        print(imc, 'está bom continue assim, você está Normal')
    elif imc >= 24.9 and imc < 30.0:
        print(imc,'você precisa estar atento, você está com Sobrepeso')
    else:
        print(imc, 'você precisa perder peso URGENTE, está Obeso')


