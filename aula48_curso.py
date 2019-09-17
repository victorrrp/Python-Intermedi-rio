'''
Criando, lendo, escrevendo e apagando arquivos
'''


#modo básico
#foi aberto um arquivo para escrita e o w+ para leitura e escrita
file = open('abc.txt', 'w+') 

#escrevendo, no caso, três linhas
file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')

#lendo (executando) todas as linhas
file.seek(0, 0) #parâmetro para determinar a posiçao do meu cursor
print('Lendo linhas: ')
print(file.read()) #para ler o arquivo e retornar uma string
print('##############')

#lendo (executando) linha por linha
file.seek(0, 0) 
print(file.readline())
print(file.readline())
print(file.readline())

#outra forma de executar linha por linha
file.seek(0, 0)
for linha in file.readlines():
    print(linha)
#fechando meu arquivo
file.close()

'''Outra forma de utilizar arquivos'''

try:
    file = open('abc.txt', 'w+')
    file.write('Linha')
    file.seek(0) #é necessário utilizar o file.seek(0)
    print(file.read())
finally:
    file.close()


'''Utilizando os gerenciadores de contexto (modo mais utilizado)'''
#o with fecha o arquivo automaticamente sem precisar do file.close

with open('abc.txt', 'w+')as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')

    file.seek(0)
    print(file.read())

#a+ - adiciona ao final do arquivo toda vez q for executado

'''importando JSON'''

import json

d1 = {
    'Pessoa 1': {
        'nome': 'Luiz',
        'idade': 25,
    },
    'Pessoa 2': {
        'nome': 'Rose',
        'idade': 30,
    },
    'Pessoa 3': {
        'nome': 'Joao',
        'idade': 44,
    },
}

d1_json = json.dumps(d1, indent=True)

with open('abc.json', 'w+') as file:
    file.write(d1_json)