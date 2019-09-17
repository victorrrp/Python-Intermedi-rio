'''
Dicionário em Python (ou chave)
'''

#Criando um dicionário (formato padrão)
d1 = {'chave1':'valor da chave'}
d1['nova_chave'] = 'Valor da nova chave'

print(d1['chave1']) #acessando indice da chave


#Outra forma
d2 = dict(chave1 = 'Valor da chave', chave2 = 'Valor da outra chave')
d2['nova_chave'] = 'Valor da nova chave'

print(d2)


#cada chave tem que ter seu próprio valor
d3 = {1: 'valor', 2: 'valor', 3: 'valor real da chave'}

print(d3)

#dicionário com valores imutáveis (por exemplo, tuplas)
d4 = {
    'str' : 'valor',
    123: 'Outro valor',
    (1,2,3,4): 'Tupla',
}

print(d4[(1,2,3,4)])#utiliza-se os colchetes para acessar o(s) valor(es) da chave

'''
caso queira deletar alguma chave, utilize:

del d4['str']

print(d4)
'''


#iterando com for
d5 = {
    'chave3' : 'valor',
    'chave4' : 'Outro valor',
    'chave5' : 'Tupla',
}

for k in d5:
    print(k)


#for k in d5.values == acessando somente os valores das chaves
#for k in d5.items == acessando tanto a chave quanto os valores
#for k, v in d5.items == desempacotando a chave
#   print(k, v)


#construindo um dicionário mais complexo
#modo de criar um dicionário dentro de outro dicionario
clientes = {
    'cliente1': {
        'nome': 'Victor',
        'sobrenome': 'Pereira',
    },
    'cliente2':{
        'nome': 'Joao',
        'sobrenome': 'Moreira',
    },
}


#modo de fazer iteração em dicionários dentro de outro dicionário
for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}') #\t para identar


#convertendo lista (também serve com tuplas, só trocar colchetes por parênteses) em dicionário
lista = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3],
]

d7 = dict(lista)
print(d7)

'''
para concatenar dicionários utilize .update, exemplo:

d1 = {
    1: 2,
    3: 4,
    5: 6,
}

d2 = {
    'a': 'b',
    'c': 'd',
}
d1.update(d2)
print(d1)
'''