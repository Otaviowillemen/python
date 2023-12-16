notas = []
quant_aluno = int(input('Quantos tem na classe?'))

for x in range(quant_aluno):
    codigo_aluno = input('RM: ')
    nota = float(input('Nota: '))
    if nota >= 6.0:
        print(codigo_aluno,'APROVADO')
    else:
        print(codigo_aluno,'REPROVADO')
    resultado = [codigo_aluno, nota]
    notas.append(resultado)
    
print('Quantidade de notas é ', len(notas))

for n in notas:
    codigo_aluno = n[0]
    nota = n[1 ]
    print('O RM ', codigo_aluno, 'tirou a nota: ',nota)