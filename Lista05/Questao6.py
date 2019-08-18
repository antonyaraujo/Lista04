'''Fazer um programa que leia 15 valores reais e os armazene em um vetor/estrutura B. Seu programa
deverá passar o vetor para a função extremos (). A função “extremos ()” deverá encontrar as posições
onde estão o maior e o menor valor existente no vetor. A função principal deverá imprimir o maior e
o menor valor bem como as respectivas posições no vetor.'''

def extremos(vetor):
    maior, menor = 0, vetor[0]
    for e in range(len(vetor)):
        if vetor[e]  > maior:
            maior = vetor[e]
        if vetor[e] < menor:
            menor = vetor[e]
    # menor = min(vetor)
    # maior = max(vetor)
    return(maior, menor)

B = []
for i in range(15):
    valor = float(input("Informe o valor real %i: " %(i+1)))
    B.append(valor)

maior = extremos(B)[0]
menor = extremos(B)[1]
print("O maior valor é", maior)
print("O menor valor é", menor)

for i in range(len(B)):
    if maior == B[i]:
        print("O maior valor está na %iª posição do vetor" % (i+1))
    if menor == B[i]:
        print("O menor valor está na %iª posição do vetor" % (i+1))