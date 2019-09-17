'''
Zip - Unindo iteráveis
Zip_longest - Itertools
'''
from itertools import zip_longest #importando módulo

#modo por extenso de se usar o zip com gerador
capitais = ['Rio de Janeiro', 'São Paulo', 'Salvador', 'Monte Belo']

estados = ['RJ', 'SP', 'BA']

capitais_estados = zip(capitais, estados)
print(next(capitais_estados))


#modo simplificado e mais frequente
capitais = ['Rio de Janeiro', 'São Paulo', 'Salvador', 'Monte Belo']

estados = ['RJ', 'SP', 'BA']

capitais_estados = zip(capitais, estados)

for valor in capitais_estados:
    print(valor[0], valor[1])
    

#utilizando com tuplas
capitais = ['Rio de Janeiro', 'São Paulo', 'Salvador', 'Monte Belo']

estados = ['RJ', 'SP', 'BA']

capitais_estados = zip(capitais, estados)

for valor in capitais_estados:
    print(valor)
    

#utilizando com listas
capitais = ['Rio de Janeiro', 'São Paulo', 'Salvador', 'Monte Belo']

estados = ['RJ', 'SP', 'BA']

capitais_estados = zip(capitais, estados)

print(list(capitais_estados))

#utilizando com dicionários
capitais = ['Rio de Janeiro', 'São Paulo', 'Salvador', 'Monte Belo']

estados = ['RJ', 'SP', 'BA']

capitais_estados = zip(capitais, estados) #é possivel trocar a ordem somente alterando as variaveis

print(dict(capitais_estados))
    

#Utilizando zip_longest - inclui todo elemento que estiver sobrando em alguma lista (importar módulo) 
capitais = ['Rio de Janeiro', 'São Paulo', 'Salvador', 'Monte Belo']

estados = ['RJ', 'SP', 'BA']

capitais_estados = zip_longest(capitais, estados)

print(list(capitais_estados))

 
