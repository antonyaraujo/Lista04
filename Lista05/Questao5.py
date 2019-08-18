'''Durante uma corrida de automóveis com N voltas de duração, foram anotados em um arquivo para
um piloto, na ordem, os tempos registrados em cada volta. Fazer um programa que leia o número de
voltas de uma corrida, e leia o tempo de cada uma das N voltas de um piloto e armazene-os em um
vetor. Seu programa deve conter uma única função para calcular: Use TDD.
    * Melhor tempo;
    * A volta em que o menor tempo ocorreu;
    * Tempo médio das N voltas;
'''
import math

voltasCorridas = int(input("Informe a quantidade de voltas da Corrida: "))
assert isinstance(voltasCorridas, int)
assert voltasCorridas != None

tempoVoltas = []
assert isinstance(tempoVoltas, list)
assert tempoVoltas != None

with open('Voltas.txt', "a+") as voltas:
    assert voltas != None
    voltas.write("\nCorrida de %i voltas - Piloto 1\n" %(voltasCorridas))
    for i in range(voltasCorridas):
        assert 0 <= i < (voltasCorridas)
        tempo = float(input("Informe o tempo da volta %i: " %(i+1)))
        assert isinstance(tempo, float)
        assert tempo != None
        tempoVoltas.append(tempo)
        assert tempoVoltas[i] == tempo
        voltas.write("Volta %i: %.2f segundos\n" %(i+1, tempo))

def melhorTempo(tempoVoltas):
    return max(tempoVoltas)

def voltaMenorTempo(tempoVoltas):
    menor = 0
    for i in range(1, len(tempoVoltas)):
        if tempoVoltas[i] < tempoVoltas[menor]:
            menor = i
            assert 0 <= menor <= tempoVoltas[i]
    return menor+1

def tempoMedio(tempoVoltas):
    soma = 0
    for t in range(len(tempoVoltas)):
        soma += tempoVoltas[t]
        assert soma >= tempoVoltas[t]
    return soma/len(tempoVoltas)

print("O melhor tempo foi de %.2fs" %(melhorTempo(tempoVoltas)))
print("A volta com o menor tempo foi a ", voltaMenorTempo(tempoVoltas), "ª volta")
print("O tempo médio das %i voltas foi de %.2fs" %(voltasCorridas, tempoMedio(tempoVoltas)))