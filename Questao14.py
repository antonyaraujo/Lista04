'''Escreva um programa que contenha um procedimento que recebe como parâmetro um número inteiro, calcule e
exiba na tela a soma de todos os algarismos deste número.'''

def somaAlgarismos(numero):
    soma = 0
    if 0 < numero <= 9:
        soma = numero
    elif 10 <= numero <= 99:
        soma = numero//10 + numero%10
    elif 100 <= numero <= 999:
        soma = numero//100 + numero%100
    print(soma)

somaAlgarismos(25)