'''Dizemos que uma matriz quadrada inteira é um quadrado mágico se a soma dos elementos de cada
linha, a soma dos elementos de cada coluna e a soma dos elementos das diagonais principal e
secundária são todas iguais.

Escreva um programa que leia uma estrutura de dados bidimensional 5x5 e passe-a para uma função
que deve retornar 1 se ela é um quadrado mágico e 0 em caso contrário. A função principal deve
imprimir uma mensagem informando se a estrutura de dados bidimensional é ou não um quadrado
mágico.'''

def quadradoMagico(A):
    principal = 0
    for i in range(len(A)):
        principal += A[i][i]

    secundario = 0
    for i in range(len(A)):
        secundario += A[i][2-i]

    if secundario != principal:
        return 0

    for i in range(len(A)):
        linha = 0
        for j in range(len(A[i])):
            linha += A[i][j]
        if linha != secundario:
            return 0

    for i in range(len(A)):
        coluna = 0
        for j in range(len(A[i])):
            coluna += A[i][j]
            break

    return 1

A = [[8,0,7],[4,5,6],[3,10,2]]
'''for i in range(3):
    lista = []
    for j in range(3):
        valor = -1
        while valor < 0:
            valor = int(input("Informe o valor da posição %ix%i: " %(i+1, j+1)))
        lista.append(valor)
    A.append(lista)'''

print(quadradoMagico(A))