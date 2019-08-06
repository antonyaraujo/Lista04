''' . Escreva um programa para ajudar profissionais da área esportiva a calcular o valor da frequência cardíaca mínima
de treinamento para potência aeróbica. Escreva um programa que contenha uma função. Esta função deve
receber por parâmetro dois valores (os valores da idade e da frequência cardíaca de repouso (FCR)), calcular a
frequência cardíaca mínima de treinamento para potência aeróbica e retornar o valor encontrado. Repetir a
chamada da função com a passagem de parâmetros e impressão do resultado enquanto não for digitado um
número negativo para a idade.
Dado: FCT = FCR + 0.6 x ((220 – idade) – FCR)
'''

def FCT(idade, fcr):
    return fcr + 0.6*((220-idade) - fcr)

idade = int(input("Informe a idade: "))
fcr = int(input("Informe a FCR: "))
while idade >= 0:
    print("Frequência cardíaca mínima de Treinamento: ", FCT(idade, fcr))
    idade = int(input("Informe a idade: "))
    fcr = int(input("Informe a FCR: "))