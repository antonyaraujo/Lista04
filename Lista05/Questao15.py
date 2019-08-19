'''Na teoria dos sistemas, define-se como elemento minimax de uma estrutura de dados bidimensional
o menor elemento da linha onde se encontra o maior elemento da estrutura de dados bidimensional.
Escreva um programa que leia uma estrutura de dados bidimensional 10 X 10 de inteiros e passe-a
para uma função que deve encontrar e retornar seu elemento minimax.'''

def minimax(A):
    maior, linhaMaior = 0, 0
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] > maior:
                maior = A[i][j]
                linhaMaior = i

    menor = A[linhaMaior][0]
    for l in range(len(A[linhaMaior])):
        if A[linhaMaior][l] < menor:
            menor = A[linhaMaior][l]

    return menor

A = []
for i in range(10):
    lista = []
    for j in range(10):
        valor = -1
        while valor < 0:
            valor = int(input("Informe o valor da posição %ix%i: " %(i+1, j+1)))
        lista.append(valor)
    A.append(lista)

print("O minimax da Matriz é: ", minimax(A))