''' Escreva um programa que contenha uma função que receba como parâmetro um número inteiro e retorne
verdadeiro caso este número seja primo, e falso, caso contrário. A função principal deve exibir adequadamente na
tela uma resposta ao usuário informando se o número digitado é primo ou não.'''

def ePrimo(numero):
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

numero = int(input("Informe um número: "))
if (ePrimo(numero)):
    print("É primo")
else:
    print("Não é primo")
