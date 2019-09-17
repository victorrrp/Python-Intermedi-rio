'''Problemas dos parâmetros mutáveis em funções'''
#objetos mutaveis - listas, dicionarios
#objetos imutaveis - tuplas, strings, numeros, True, False, None

#resolução do problema
def lista_de_clientes(clientes_iteravel, lista=[]):
  lista.extend(clientes_iteravel)
  return lista

lista_de_clientes_1 = ['Fabricio']
clientes1 = lista_de_clientes(['João', 'Maria', 'Eduardo'], lista_de_clientes_1)
clientes2 = lista_de_clientes(['Marcos', 'Jonas', 'Zico'])  

print(clientes1)
print(clientes2)