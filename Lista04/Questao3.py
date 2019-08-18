''' Escreva um programa que leia um número A (representando o número de alqueires) e uma letra (P para Paulista,
M para Mineiro e B para Baiano). O programa deve chamar uma função que recebe por parâmetro o número A e o
caractere lido, e converte A para um valor em metros quadrados, e retorna o valor encontrado segundo as
informações dadas logo abaixo. A função principal deve mostrar na tela o valor retornado.
Dado:
1 alqueire Paulista = 24200 m2
1 alqueire Mineiro = 48400 m2
1 alqueire baiano = 96 800 m2'''

def conversor(numero, letra):
    if letra == 'P':
        return numero/24200
    elif letra == 'M':
        return numero/48400
    elif letra == 'B':
        return numero/96800

A = int(input("Informe o número de alqueires: "))
letra = (input("Informe uma letra: "))
print("O valor é: %.2fm²" %(conversor(A, letra)))
