'''
Função filter - Bem parecida com a função map, porém ela retorna 
verdadeiro ou falso para expressão que você 'falar'
'''

#utilizando filter
from aula40_curso import produtos, pessoas, lista

nova_lista = filter(lambda x: x > 5, lista)
print(list(nova_lista))


#fazendo o mesmo processo só que em list comprehension
nova_lista = [x for x in lista if x > 5]
print(list(nova_lista))
print()

#utilizando filter buscando somente de prdutos com preços acima de 20
nova_lista = filter(lambda p: p['preço'] > 20, produtos)

for produto in nova_lista:
    print(produto)

#utilizando filter de forma mais complexa
def filtra(produto):
    if produto['preço'] > 20:
        produto['eh_caro'] = True #acrescentando um iteravel
    return True

nova_lista = filter(filtra, produtos)

for produto in nova_lista:
    print(produto)
