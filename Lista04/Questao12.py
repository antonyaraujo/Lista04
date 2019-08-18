''' Escreva um programa que contenha uma função que receba dois valores inteiros n1 e n2 (assuma n1 sempre
maior que n2) e retorne a soma de todos os valores pares entre n1 e n2 (inclusive ambos, se for o caso). A função
principal deve imprimir o resultado obtido.'''

def somaPares(n1, n2):
    soma = 0
    for i in range(n1, n2+1):
        if i % 2 == 0:
            soma += i
    return soma

n1 = int(input("informe o valor 1: "))
n2 = int(input("informe o valor 2: "))
print(somaPares(n1, n2))
