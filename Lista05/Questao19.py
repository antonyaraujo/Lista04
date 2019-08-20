''' Faça um programa, que leia em uma matriz a população dos 10 municípios mais populosos de cada
um dos 26 estados brasileiros. Passe a matriz para uma função que determina e imprime o número
de habitantes do município mais populoso e o número do estado a que pertence. Considerando que
a primeira coluna contém sempre a população da capital do estado, calcular e retornar a média da
população das capitais dos 26 estados. Pode usar listas. Use dicionário.'''

populacao = []
for i in range(2):
    lista = []
    for j in range(2):
        valor = -1
        while valor < 0:
            valor = int(input("Informe a população de %ix%i: " %(i+1, j+1)))
        lista.append(valor)
    A.append(lista)