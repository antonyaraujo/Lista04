''' Escreva um programa que leia duas estruturas de dados unidimensionais ordenadas crescentemente
A e B de 10 posições e passe-as para uma função que deve construir uma nova estrutura de dados
unidimensional C ordenada crescentemente com os elementos de A e B. '''

def ordenacaoC(A, B):
    C = []
    for i in range(5):
        C.append(A[i])
        C.append(B[i])

    for i in range(10):
        if i > 0:
            if C[i] < C[i-1]:
                aux = C[i-1]
                C[i-1] = C[i]
                C[i] = aux
    return C

vetorA, vetorB = [], []
for i in range(5):
    valor = int(input("Informe o valor %i do vetor A" %(i)))
    vetorA.append(valor)

for i in range(5):
    valor = int(input("Informe o valor %i do vetor B" % (i)))
    vetorB.append(valor)

C = ordenacaoC(vetorA, vetorB)
print(vetorA)
print(vetorB)
print(C)