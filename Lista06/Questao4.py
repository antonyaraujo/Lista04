'''Faça um programa que contenha uma função. Essa função deve receber uma string, dois números
inteiros (representando posição inicial e posição final). A função deve construir uma substring da
string recebida por parâmetro, sendo que esta substring é o intervalo, na string original, entre os
dois valores também recebidos por parâmetro (inicial e final). Ao final a função deve imprimir na tela
esta substring construída. Copie um caracter por vez.
Exemplo: Se for digitada a string PROGRAMACAO e os valores 4 e 8 deverá ser impresso na tela a
substring GRAMA.'''

def substring(string, n1, n2):
    return string[n1-1:n2]

print(substring("PROGRAMACAO", 4, 8))