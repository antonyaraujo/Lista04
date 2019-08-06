'''Faça uma função que dado um número n retorne o n-ésimo número de Fibonacci. O número de fibonacci é dado
por n0=0, n1=1, ni = ni-1+ni-2.'''

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        fibonacci = 1
        penultimo = 0
        for i in range(1, n):
            ultimo = fibonacci
            fibonacci = ultimo + penultimo
            penultimo = ultimo
        return fibonacci
numero = int(input("Informe um número: "))
print("Fibonacci: ", fibonacci(numero))