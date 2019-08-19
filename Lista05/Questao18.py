'''Escreva um programa que contenha uma função que receba via parâmetro uma estrutura de dados
bidimensional MAT de valores inteiros, que seja quadrada de ordem 10 (dez). A função deve retornar
1 se a estrutura de dados bidimensional for uma estrutura de dados bidimensional identidade e 0 em
caso contrário. 4. Dizemos que uma estrutura de dados bidimensional quadrada é uma estrutura de
dados bidimensional identidade se todos os elementos que não pertencem à diagonal principal são
todos iguais a zero e todos os elementos da diagonal principal são iguais a 1.'''

def identidade(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            if i==j:
                if Mat[i][j] != 1:
                    return 0
            else:
                if Mat[i][j] != 0:
                    return 0
    return 1

Mat = []

for i in range(10):
    lista = []
    for j in range(10):
        if i == j:
            lista.append(1)
        else:
            lista.append(0)
    Mat.append(lista)

print(identidade(Mat))