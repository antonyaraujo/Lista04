'''Escreva um programa que contenha uma função chamada mistura. Esta função recebe como
parâmetros duas strings s1 e s2 e constrói uma nova string s3 resultado da mistura das duas strings
recebidas como parâmetros. Esta mistura consiste em pegar alternadamente um caractere de cada
string começando por s1. Se uma string é maior que a outra completa-se s3 com os caracteres
restantes da string maior.'''

def mistura(s1, s2):
    tamanho1 = len(s1)
    tamanho2 = len(s2)
    s3 = []
    if tamanho1 > tamanho2:
        for i in range(tamanho2):
            s3.append(s1[i])
            s3.append(s2[i])
        s3.append(s1[i:])
    else:
        for i in range(tamanho2):
            s3.append(s1[i])
            s3.append(s2[i])
        s3.append(s2[i:])
    return "".join(s3)

print(mistura("abcdef", "gggg"))