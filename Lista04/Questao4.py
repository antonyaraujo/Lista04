''' Escreva um programa que chame uma função que deve receber por parâmetro dois valores (um para comprimento
e outro para largura), calcular e apresentar na tela a área de um retângulo, através da fórmula do retângulo =
comprimento * largura. Repetir a chamada da função com a passagem de parâmetros enquanto não for digitado
um número negativo para o comprimento ou para a largura.'''

def area(comprimento, largura):
    return comprimento * largura

comprimento = float(input("Comprimento do retângulo: "))
largura = float(input("Largura do retângulo: "))
while (comprimento > 0) and (largura > 0):
    print("A área do retângulo é: ", (area(comprimento, largura)), "m²")
    comprimento = float(input("Comprimento do retângulo: "))
    largura = float(input("Largura do retângulo: "))

