'''
Funçao - Reduce --> Função acumuladora 'compulsiva'
*Essa função não tem no python por padrão, 
dentro dos built-ins, então é necessário fazer o import
'''

from aula40_curso import produtos, pessoas, lista
from functools import reduce


#forma normal de acumular valores de, por exemplo, uma lista 
acumula = 0
for item in lista:
    acumula+= item

print(acumula)


#mesmo processo só que na função reduce
#a cada volta do laço será executada essa expressão
soma_lista = reduce(lambda acumulador, item: item + acumulador, lista, 0)
print(soma_lista)


#utilizando reduce com dicionários
soma_preços = reduce(lambda acumulador, produto: produto['preço'] + acumulador, produtos, 0)
print(round(soma_preços))


#tirando a media
soma_preços = reduce(lambda acumulador, produto: produto['preço'] + acumulador, produtos, 0)
print(round(soma_preços / len(produtos)))
