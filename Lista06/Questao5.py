''' Escreva um programa que leia uma string, um caractere e o índice de uma posição da string e
passe-os como parâmetro para uma função. A função deve inserir o caractere na string na posição
dada, "empurrando" todos os demais caracteres para a direita.'''

def inserirCaracter(texto, caracter, posicao):
    lista = list(texto)
    lista.insert(posicao, caracter)
    return "".join(lista)

print(inserirCaracter("rama", "G", 0))
