''' Escreva um programa que receba 3 números inteiros e chame uma função que retorne 0 caso os três números
estejam em ordem crescente ou 1 caso estejam em ordem decrescente. A função principal deve imprimir na tela
uma mensagem informando o resultado.'''

def ordem(n1, n2, n3):
    if n1 < n2 < n3:
        return 0
    elif n1 > n2> n3:
        return 1
    else:
        return 2

n1 = int(input("Informe o valor 1: "))
n2 = int(input("Informe o valor 2: "))
n3 = int(input("Informe o valor 3: "))
if ordem(n1, n2, n3):
    print("É decrescente")
elif ordem(n1, n2, n3) == 2:
    print("Os valores são iguais")
else:
    print("É crescente")

