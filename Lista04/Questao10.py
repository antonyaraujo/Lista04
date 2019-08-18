''' Faça uma função para calcular x elevado a y, sendo y inteiro e não negativo. Use produtos sucessivos para resolver
a questão.'''

def potencia(x, y):
    if y == 0:
        return 1
    else:
        potencia = 1
        for i in range(y):
            potencia *= x
        return potencia

x = int(input('Informe x: '))
y = -1
while y < 0:
    y = int(input('Informe y: '))
print("%i^%i = %i" %(x, y, potencia(x, y)))
