''' Escreva um programa que receba os valores correspondentes aos comprimentos de três segmentos (números
reais) e chame uma função que receba estes valores como parâmetros. Esta função deve retornar falso, caso os
valores dos segmentos informados não constituam um triângulo. Caso constituam um triângulo, chame outra
função que retorne a classificação angular do triângulo, que pode ser: acutângulo, retângulo ou obtusângulo. A
função principal deve imprimir na tela uma mensagem informando se os segmentos informados podem constituir
um triângulo ou não, e caso afirmativo, informe sua classificação angular. (Dica: Primeiro verifique se os três
segmentos podem constituir um triângulo considerando que um triângulo só existe quando o maior dos lados é
menor que a soma dos outros dois)'''
from math import sin, tan

a = float(input("Segmento a: "))
b = float(input("Segmento b: "))
c = float(input("Segmento c: "))
print(tan(8/6))
def classificacao(a, b, c):
    if (a == 90 and b != 90 and c != 90) or (a != 90 and b == 90 and c == 90) or (a != 90 and b != 90 and c == 90):
        print("Retângulo")
    elif a < 90 and b < 90 and c < 90:
        print("Acutângulo")
    elif a > 90 and b > 90 and c >90:
        print("Obtusângulo")

def triangulo(a, b, c):
    if a < b + c or b < a + c or c < a + b:
        print("É triângulo")
        maior = [a, b, c]
        if a == max(maior):
            angulo1 = sin(b/c)
            angulo2 = sin(a/c)
            angulo3 = sin(a/b)
        elif b == max(maior):
            angulo1 = sin(c / a)
            angulo2 = sin(b / a)
            angulo3 = sin(b / c)
        elif c == max(maior):
            angulo1 = sin(b / a)
            angulo2 = sin(c / a)
            angulo3 = sin(c / b)

        print(angulo1)
        print(angulo2)
        print(angulo3)
        classificacao(angulo1, angulo2, angulo3)

triangulo(a, b, c)