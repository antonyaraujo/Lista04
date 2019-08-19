'''Faça um programa que leia uma estrutura de dados bidimensional 12 x 13 de números inteiros e
positivos e passe-a para uma função que deve multiplicar todos os elementos das linhas pares pelo
maior elemento da estrutura de dados bidimensional. A função principal deve imprimir a estrutura de
dados bidimensional antes e depois da chamada da função.'''

def maiorValor(A):
    maior = 0
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] > maior:
                maior = A[i][j]
    return maior

def multiplicar(A):
    maior, B = maiorValor(A), []
    for i in range(len(A)):
        lista = []
        for j in range(len(A[i])):
            if (i+1)%2 == 0:
                lista.append(A[i][j] * maior)
            else:
                lista.append(A[i][j])

        B.append(lista)

    return B

A = []
for i in range(12):
    lista = []
    for j in range(13):
        valor = -1
        while valor < 0:
            valor = int(input("Informe o valor da posição %ix%i: " %(i+1, j+1)))
        lista.append(valor)
    A.append(lista)

print(A)
print(multiplicar(A))