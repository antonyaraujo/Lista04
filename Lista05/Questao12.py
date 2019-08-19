''' Escreva um programa que contenha uma função. Essa função deve receber por parâmetro uma
estrutura unidimensional A de inteiros de tamanho 5. A função deve construir uma outra estrutura
unidimensional B de inteiros de tamanho 5 que deverá conter o fatorial de cada elemento de A. Depois
mostrar na tela o conteúdo do vetor B.'''

def fatorial(n):
    fatorial = 1
    for i in range(1, n+1):
        fatorial *= i
    return fatorial

def funcao(A):
    B = []
    for i in range(len(A)):
        B.append(fatorial(A[i]))
    return B

A = []
for i in range(5):
    valor = int(input("Informe o valor %i: " %(i+1)))
    A.append(valor)

B = funcao(A)
print(A)
print(B)