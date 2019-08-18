''' Escreva uma função que receba dois números e retorne verdadeiro (1) ou falso (0) indicando se o primeiro número
é divisível pelo segundo'''

def divisivel(n1, n2):
    if (n1%n2 == 0):
        return 1
    else:
        return 0

n1 = float(input("Informe o número 1: "))
n2 = float(input("Informe o número 2: "))
print(divisivel(n1, n2))
