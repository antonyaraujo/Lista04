'''Escreva um programa que contenha uma função que receba como parâmetros uma frase e retorne
a quantidade de vogais existentes na string. A função principal deve imprimir o valor retornado.'''

def quantidadeVogais(frase):
    contador = 0
    for i in (frase):
        if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u' and i != " ":
            if i != 'A' and i != 'E' and i != 'I' and i != 'O' and i != 'U':
                contador += 1
    return contador

frase = input("Escreva sua frase: ")
print("Sua frase possui: ", quantidadeVogais(frase), "vogais")