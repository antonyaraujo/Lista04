'''Escreva um programa que contenha uma função MAX que recebe como parâmetros uma estrutura
de dados A de tamanho 9linhas x 5colunas e imprime três inteiros: k, Lin e Col. O inteiro k é o maior
elemento de A e Lin é a linha onde este elemento se encontra e Col é a coluna onde este elemento
se encontra'''

A = []
for i in range(9):
    lista = []
    for j in range(5):
        valor = int(input("Informe o valor %ix%i" %(i+1, j+1)))
        lista.append(valor)
    A.append(lista)

def MAX(A):
    k, Lin, Col = 0, [], []
    for i in range(9):
        for j in range(5):
            if A[i][j] >= k:
                k = A[i][j]
                Lin.append(i)
                Col.append(j)

    print("O maior valor é: ", k)
    for lc in range(len(Lin)):
        print(k, "está na linha:", Lin[lc]+1, "coluna:", Col[lc] + 1)

MAX(A)