''' Faça uma função que, dado um número representando uma temperatura em graus Fahrenheit, retorne a
temperatura em Celsius. Obs: C=(5/9)*(F-32).'''

def conversao(fahrenheit):
    return (5/9)*(fahrenheit-32)

F = float(input("Fahrenheit: "))
print("Celsius: %.1fºC" %(conversao(F)))
