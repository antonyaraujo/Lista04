'''Uma das maneiras de se conseguir a raiz quadrada de um número é subtrair do número os ímpares consecutivos a
partir de 1, até que o resultado da subtração seja menor ou igual à zero. O número de vezes que se conseguir
fazer a subtração é a raiz quadrada exata (resultado 0) ou aproximada do número (resultado negativo).

Escreva um programa que leia um inteiro e passe o valor por parâmetro para a função raiz(). A função raiz() utiliza
o método descrito acima para calcular e retornar a raiz inteira encontrada. A raiz encontrada deverá ser impressa
pelo programa principal.'''

def raiz(numero):
    subtracao = numero
    contador = 0
    for i in range(1, numero, 2):
        subtracao = subtracao - i
        contador += 1
        if subtracao == 0:
            break
    return contador

print(raiz(4))