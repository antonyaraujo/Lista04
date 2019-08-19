'''Dizemos que uma matriz quadrada inteira é um quadrado mágico se a soma dos elementos de cada
linha, a soma dos elementos de cada coluna e a soma dos elementos das diagonais principal e
secundária são todas iguais.

Escreva um programa que leia uma estrutura de dados bidimensional 5x5 e passe-a para uma função
que deve retornar 1 se ela é um quadrado mágico e 0 em caso contrário. A função principal deve
imprimir uma mensagem informando se a estrutura de dados bidimensional é ou não um quadrado
mágico.'''

def quadradoMagico(A):
    linhas, diagonais, colunas = [], [], [0, 0, 0]
    for i in range(len(A)):
        somaLinha, somaDiagonal = 0, 0
        for j in range(len(A[i])):
            somaLinha += A[i][j]
            if i == j:
                somaDiagonal += A[i][j]
            for k in range(3):
                if j == k:
                    colunas[j] += A[i][j]
        linhas.append(somaLinha)
        diagonais.append(somaDiagonal)

    print((diagonais))
    print((linhas))
    print((colunas))

    for l in range(3):
        if (diagonais[3-l] != diagonais[l]) or (linhas[3-l] != linhas[l]) or (colunas[3-l] != colunas[l]):
            return 0
    return 1


A = []
for i in range(3):
    lista = []
    for j in range(3):
        valor = -1
        while valor < 0:
            valor = int(input("Informe o valor da posição %ix%i: " %(i+1, j+1)))
        lista.append(valor)
    A.append(lista)

print(quadradoMagico(A))