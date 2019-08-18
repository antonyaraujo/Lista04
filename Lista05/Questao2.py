'''Simule a execução do programa abaixo destacando sua saída, ou seja, o que exatamente será
impresso na tela. Você deve escrever na ordem em que os dados aparecem.'''

def FazAlgo(x, y, vetor): #(12, 6, [5, 6, 7, 8]
     c = y # c = 6
     b = x % 4 # b = 0
     x = x + 2 # x = 14
     y = y + 3 # y = 9
     print("\n {} {} {} {} {}".format(b, x, y, vetor[b], c)) # Imprime: 0 14 9 5 6
     return y

a = 5
b = 6
c = 7
vetor = []

for i in range(4):
     vetor.append(i+a)

# i = 0 --> vetor[5]
# i = 1 --> vetor[5,6]
# i = 2 --> vetor[5,6,7]
# i = 3 --> vetor[5,6,7,8]

print("Os valores do vetor são: \n")

for i in range(4):
     print(vetor[i]) #5, 6, 7, 8


b = FazAlgo(a + c, b, vetor) # a + c = 12, b = 6, vetor = [5, 6, 7, 8]
print("\n {} {} {}".format(a,b,c));

# Saída Final
'''
5
6
7
8

0 14 9 5 6

5, 9, 7
'''