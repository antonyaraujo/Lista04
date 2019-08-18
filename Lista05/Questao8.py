''' Faça uma função que receba, como parâmetros, uma estrutura de dados com números inteiros e seu
tamanho, e retorne 1 se o vetor estiver ordenado de forma crescente e 0 se não estiver.'''

def ordenacao(vetor, tamanhovetor):
    crescente = 1
    for i in range(tamanhovetor):
        if i > 0:
            if vetor[i-1] > vetor[i]:
                crescente = 0
    return crescente

tamanho = int(input("Informe o tamanho do vetor: "))
vetor = []
for i in range(tamanho):
    valor = int(input("Informe o valor %i do vetor: " %(i+1)))
    vetor.append(valor)

print(ordenacao(vetor, tamanho))