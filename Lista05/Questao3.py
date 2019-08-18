'''Escreva um programa que contenha uma estrutura chamada Horário capaz de armazenar horas,
minutos e segundos. Seu programa deverá conter uma função que recebe um horário como
parâmetro e altera-o para quando começar o horário de verão.'''
from datetime import datetime

'''def horario_atual():
    horas = datetime.now().hour
    minutos = datetime.now().minute
    segundos = datetime.now().second
    print(horas,":",minutos,":",segundos)
    return (horas, minutos, segundos)'''

def horario():
    hora = int(input("Informe a hora: "))
    minuto = int(input("Informe os minutos: "))
    segundo = int(input("Informe os segundos: "))
    return (hora, minuto, segundo)

def horarioVerao(hora):
    horario = hora+1
    return horario

tupla = horario()
print("O horário de verão é: %i:%i:%i" %(horarioVerao(tupla[0]), tupla[1], tupla[2]))