'''
Groupby - Agrupando elementos num dicionário
'''
#é nececessário importar as linhas de código para cada situação
from itertools import groupby

#abrindo uma lista para criar dicionários dentro
alunos = [
    {'nome':'Luiz', 'nota':'A'},
    {'nome':'Carlos', 'nota':'B'},
    {'nome':'Rodrigo', 'nota':'F'},
    {'nome':'Luiza', 'nota':'C'},
    {'nome':'Larissa', 'nota':'A'},
    {'nome':'Cecília', 'nota':'B'},
    {'nome':'Victor', 'nota':'B'},
    {'nome':'Karina', 'nota':'D'},
    {'nome':'Gabriel', 'nota':'C'},
    {'nome':'Arrascaeta', 'nota':'A'},
    {'nome':'Gerson', 'nota':'F'},
]

#manipulando o dicionario original colocando a função lambda
ordena = lambda item: item['nota']
alunos.sort(key=ordena)

for aluno in alunos:
    print(aluno)


#agrupando os dados em dicionários separados verificando a qtd de alunos em cada agrupamento de nota
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    print(f'Agrupamento: {agrupamento}')

    quantidade = len(list(valores_agrupados)) #foi necessário colocar o 'list' porque o "valores_agrupados" é um objeto retornado pela groupby
    print(f'{quantidade} alunos tiraram a nota {agrupamento}')
