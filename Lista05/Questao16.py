''' Escreva um programa que leia duas estruturas de dados unidimensionais ordenadas crescentemente
A e B de 10 posições e passe-as para uma função que deve construir uma nova estrutura de dados
unidimensional C ordenada crescentemente com os elementos de A e B. '''

def ordenacaoC(A, B):
    C = []
    for i in range(5):
        C.append(B[i])
        C.append(A[i])

    D = C
    '''
    Selection Sort
    for i in range(len(D)):
        menor = i
        for j in range(i, len(D)):
            if D[j] < D[menor]:
                menor = j

        aux = D[menor]
        D[menor] = D[i]
        D[i] = aux

    print(D)'''

    # Bubble Sort
    for decrescente in range(10, 0, -1):
        for atual in range(0, decrescente -1):
            if C[atual] > C[atual+1]:
                aux = C[atual+1]
                C[atual+1] = C[atual]
                C[atual] = aux

    return C

'''vetorA, vetorB = [], []
for i in range(5):
    valor = int(input("Informe o valor %i do vetor A" %(i)))
    vetorA.append(valor)

for i in range(5):
    valor = int(input("Informe o valor %i do vetor B" % (i)))
    vetorB.append(valor)
'''
vetorA = [1,2,3,4,5]
vetorB = [5,4,3,2,1]
C = ordenacaoC(vetorA, vetorB)
print(vetorA)
print(vetorB)
print(C)