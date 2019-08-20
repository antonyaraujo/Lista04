'''Escreva um programa que contenha uma função. Essa função deve receber como parâmetro uma
palavra e retorna 1 se palavra é palíndromo e 0 em caso contrário. Uma palavra é palíndromo
quando apresenta a mesma grafia quando lida a partir do início ou de trás para diante; exemplo:
RIR, SOLOS, ASA, RALAR, ANNA, ARARA. A função principal deve imprimir uma mensagem
informando se a palavra é ou não um palíndromo'''

def palindromo(palavra):
    tamanho, inverso = len(palavra), []
    for i in range((len(palavra)-1), -1, -1):
        inverso.append(palavra[i])
    inverso = "".join(inverso)
    print(palavra)
    print(inverso)
    if palavra == inverso:
        return 1

    return 0

if palindromo("AsA"):
    print("É palíndromo")
else:
    print("Não é palíndromo")