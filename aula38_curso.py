'''
Itertools
Combinations - Ordem não importa
Permutations - Ordem importa
Ambos não repetem valores unicos
Product - Ordem importa e repete valores únicos
'''
#é nececessário importar as linhas de código para cada situação

from itertools import combinations, permutations, product

#Supondo que o usuário queira saber quais são as combinações, permutações e produtos possiveis
pessoas = ['Luiz', 'André', 'Victor', 'Eduardo', 'Leticia', 'Fabricio', 'Rose']


#fazendo combinação (quando a ordem não importa)
for grupo in combinations(pessoas, 2):
    print(grupo) 
print()

#fazendo permutação (quando a ordem importa)
for grupo in permutations(pessoas, 2):
    print(grupo)
print()

#fazendo produto (quando a ordem importa e deseja-se repetição de valores únicos)
for grupo in product(pessoas, repeat=2):
    print(grupo)
