'''Uma floricultura, conhecedora de sua clientela, gostaria de fazer um programa que pudesse controlar
sempre um estoque mínimo de determinadas plantas, pois todo dia, pela manha, o dono faz novas
aquisições. Criar um programa que deixe cadastrar 50 tipos de plantas e nunca deixar o estoque ficar
abaixo do ideal. Para cada planta, o dono gostaria de cadastrar um código, o estoque ideal e a
quantidade em estoque. Escreva um programa que leia as informações das 50 plantas e armazeneas em uma matriz.
Em seguida, passe esta matriz para uma função que deve calcular a quantidade
que o dono da loja precisa comprar de cada produto no próximo dia. Implemente duas soluções, uma
só com listas e outra, também com dicionários.'''



tiposPlantas = {}
for i in range(1):
    for j in range(5):
        codigo = int(input("Insira o código da planta: "))
        estoqueIdeal = int(input("Insira a quantidade de estoque ideal: "))
        quantidadeEstoque = int(input("Insira a quantidade em estoque: "))
        tiposPlantas[(i, j)] = [codigo, estoqueIdeal, quantidadeEstoque]

print(tiposPlantas)