'''
*Split - Dividir uma string gerando uma lista
*Join - Transformar uma lista numa string
*Enumerate - Enumerar elementos da lista
'''


string1 = 'O Brasil é penta.' # string sem alteraçãos
lista1 = string1.split(' ') # utilizando split
string2 = ','.join(lista1) # utilizando join

print(string1)
print(lista1)
print(string2)


#demonstrando como o enumerate trabalha
lista = [
    [0, 'O'],
    [1,'Brasil'],
    [2,'é'],
    [3, 'penta'],
]
for indice, nome in lista:
    print(indice, nome)



#utilizando enumerate
string = ['O', 'Brasil', 'é', 'penta']
for indice, valor in enumerate(string):
    print(indice, valor)



#lista dentro de lista
lista = [
    [1,2],
    [3,4],
    [5,6],
]
for v in lista:
    print(v) #é possivel acessar o indice. ex.: print(v[0], v[1])


#forma de desempacotamento de lista
lista = ['Victor', 'Joao', 'Maria']

n1, n2, n3 = lista

print(n2)