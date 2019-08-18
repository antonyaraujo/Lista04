''' Escreva um programa que leia duas estruturas de dados com o formato 10linhasx10colunas
e passe-as para uma função que deve retornar 1 se as estruturas são iguais e 0 em caso contrário. A função
principal imprime uma mensagem baseada no valor retornado.'''

def matrizesIguais(matrizA, matrizB):
    for i in range(2):
        for j in range(2):
            if matrizA[i][j] != matrizB[i][j]:
                return 0

    return 1

matrizA = []
matrizB = []

for i in range(2):
    linha = []
    for j in range(2):
        linha.append(0)
    matrizA.append(linha)

for i in range(2):
    linha = []
    for j in range(2):
        linha.append(1)
    matrizB.append(linha)

for i in range(2):
    for j in range(2):
        matrizA[i][j] = float(input("Matriz A: Informe o item o item na posição %ix%i" %(i+1, j+1)))
        matrizB[i][j] = float(input("Matriz B: Informe o item o item na posição %ix%i" % (i + 1, j + 1)))

for i in range(2):
    for j in range(2):
        print("%.2f  " %matrizA[i][j], end="")

    print("         ", end="")

    for j in range(2):
        print("%.2f  " % matrizB[i][j], end="")

    print()

if matrizesIguais(matrizA, matrizB):
    print("São exatamente iguais")
else:
    print("Não são iguais")