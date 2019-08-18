''' Escreva um programa que contenha uma função que receba como parâmetros um caractere representando uma
operação matemática (+,-,/,*) e dois números reais representando os operandos. Sua função deve efetuar a
operação dada sobre os operandos e retornar o resultado. A função principal deve imprimir o resultado. (Obs.:
cuidado com a divisão por 0) '''

def calculadora(operacao, n1, n2):
    if operacao == '+':
        print("%.2f + %.2f = %.2f" %(n1, n2, n1 + n2))
    elif operacao == '-':
        print("%.2f - %.2f = %.2f" %(n1, n2, n1 - n2))
    elif operacao == '*':
        print("%.2f x %.2f = %.2f" %(n1, n2, n1 * n2))
    elif operacao == '/':
        try:
            print("%.2f ÷ %.2f = %.2f" %(n1, n2, n1 / n2))
        except ZeroDivisionError:
            print("Não há divisão por zero")

operacao = input("Informe o tipo da operação: ")
n1 = float(input("Informe o valor 1: "))
n2 = float(input("Informe o valor 2: "))
calculadora(operacao, n1, n2)
