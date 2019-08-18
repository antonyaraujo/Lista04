'''Escreva um programa que leia um valor na unidade copos e faça uma chamada a uma função
chamada liquido que deve determinar o número de galões, quartos e pints equivalentes ao valor em
copos. Em seguida os valores obtidos devem ser impressos no programa principal. Utilize a relação
de 2 copos para 1 pint, 4 copos para 1 quarto e 16 copos para 1 galão.'''

copos = int(input("Informe a unidade de copos: "))

def liquido(copos):
    pint = copos/2
    quarto = copos/4
    galao = copos/16
    return (pint, quarto, galao)

print("%i copo(s) é equivalente à: " %(copos))
print("%i pint(s)" %(liquido(copos)[0]))
print("%i quarto(s)" %(liquido(copos)[1]))
print("%i galão(s)" %(liquido(copos)[2]))