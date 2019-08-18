''' Escreva um programa que receba três números inteiros (a,b,c) correspondentes aos coeficientes de uma equação
do tipo ax2 + bx + c. Chame um procedimento que receba estes números como parâmetros e calcule o delta desta
equação, informando se existem raízes reais ou não, e caso existam, exiba estas raízes. (Dica: Use o módulo math
para calcular as raízes no programa. Obs: Delta < 0 - Não existem raízes reais, Delta = 0 - Existe uma única raíz,
Delta > 0 - Existem duas raízes reais)'''

from math import sqrt

def grau2(a, b, c):
    delta = (b**2) - (4*a*c)
    if delta > 0:
        raiz1 = ((-b) + sqrt(delta))/(2*a)
        raiz2 = ((-b) - sqrt(delta))/(2*a)
        print("x' = %.1f" %(raiz1))
        print("x'' = %.1f" % (raiz2))
    elif delta == 0:
        raiz = ((-b) + sqrt(delta))/(2*a)
        print("x: %.1f" %(raiz))
    else:
        print("Não há raízes reais")

a = float(input("Informe o coeficiente a: "))
b = float(input("Informe o coeficiente b: "))
c = float(input("Informe o coeficiente c: "))
print("A equação %.1fx² + %.1fx + %.1f tem raízes: " %(a, b, c))
grau2(a, b, c)
