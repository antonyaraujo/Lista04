'''Faça um programa que leia uma estrutura de dados bidimensional 5 x 5 com números reais e passea
para uma função que deve construir uma estrutura de dados unidimensional que conterá os
menores elementos de cada linha. A função deve imprimir a estrutura de dados unidimensional
encontrado.'''

def menoresLinha(matriz):
    menores = []
    for i in range(len(matriz)):
        menor = matriz[i][0]
        for j in range(len(matriz[i])):
            if matriz[i][j] < menor:
                menor = matriz[i][j]
        menores.append(menor)
    return menores

A = []
for i in range(5):
    lista = []
    for j in range(5):
        valor = -1
        while valor < 0:
            valor = float(input("Informe o valor da posição %ix%i: " %(i+1, j+1)))
        lista.append(valor)
    A.append(lista)

menores = menoresLinha(A)
print(menores)
