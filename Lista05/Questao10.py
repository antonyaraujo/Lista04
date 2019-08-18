'''Faça uma função que receba estrutura de dados com 10 números e informe a quantidade de
ocorrências do último número lido. Por exemplo, para a sequência 38 4 23 5 6 7 4 12 4, o resultado
deve ser ‘O número 4 apareceu 3 vezes’.'''

def ocorrencias(vetor):
    numero = vetor[len(vetor)-1]
    ocorrencia = 0
    for i in range(len(vetor)):
        if vetor[i] == numero:
            ocorrencia += 1
    return (numero, ocorrencia)

n = int(input("Informe o tamanho do vetor: "))
vetor = []
for j in range(n):
    elemento = float(input("Informe o número %i: " %(j+1)))
    vetor.append(elemento)

tupla = ocorrencias(vetor)
print("O valor %.1f apareceu %i vezes" %(tupla[0], tupla[1]))
