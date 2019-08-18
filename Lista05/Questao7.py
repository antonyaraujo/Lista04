''' Escreva um programa que contenha uma função que recebe um número inteiro n > 0 e devolve o
número de dígitos de n e o primeiro dígito de n. Escreva um programa que lê uma sequência de N
inteiros positivos e imprime o número de dígitos e o primeiro dígito de cada um deles. Use TDD. '''

n = -1
while n < 0:
    n = int(input("Informe um valor inteiro N: "))
    assert n > 0
    assert isinstance(n, int)

numero = n
primeiro = 0
c = 0

while n > 0:
    c += 1
    if (n//10 == 0):
        primeiro = n
        assert(primeiro != 0)
    n = n//10

assert n == 0
print("O número %i possui %i digitos " %(numero, c))
print("O primeiro dígito de %i é %i" %(numero, primeiro))