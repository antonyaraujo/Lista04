'''Faça uma função que receba um vetor/lista de 100 elementos e retorne a média ponderada, onde os
pesos de cada valor é dado pelo seu índice no vetor.'''

lista, valores, soma = [], 0, 0
for p in range(1, 6):
    x = int(input(("Informe o elemento %i: ") %(p)))
    x = x*p
    valores += p
    lista.append(x)

print("A média ponderada da lista é: %.2f" %(sum(lista)/valores))

