'''
Escreva um programa que contenha uma função que receba um número inteiro N maior ou igual a 2 como
parâmetro e retorne o maior número primo menor ou igual ao número passado à função. A função principal deve
imprimir este resultado. (Dica: use a questão 12 como função auxiliar)
'''
from Questao13 import ePrimo

def maiorPrimo(N):
     if ePrimo(N):
         return N
     else:
         for i in range(N, 0, -1):
             if ePrimo(i):
                 return i

numero = 1
while numero < 2:
    numero = int(input("Informe um valor N maior ou igual a 2: "))

print(maiorPrimo(numero))