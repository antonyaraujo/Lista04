'''Escreva um programa que leia um número e contenha uma função. Esta função deve receber por parâmetro um
número, verificar e retornar o valor 1 se o número for solução da equação 2x2 - 7x + 3 = 0. Caso o número não
seja solução da equação, retornar o valor zero. A função principal deve recebe o valor de retorno e imprimir uma
mensagem informando se o valor é ou não solução da equação.'''

def equacao(numero):
    equacao = 2*(numero)*2 - 7*(numero) + 3
    if equacao == 0:
        return 1
    else:
        return 0

x = float(input("Insira um número: "))
if equacao(x) == 1:
    print("%.1f é a solução da equação" %(x))
else:
    print("%.1f não é a solução da equação" % (x))
