'''Desempacotamento de listas em Python'''


#desempacotamento de lista
lista = ['Victor', 'Joao', 'Maria']

n1, n2, n3 = lista #se não colocar as variaveis, o programa não roda

print(n2)



#desempacotamento de lista jogando os valores em outra lista evitando erro
lista = ['Victor', 'Joao', 'Maria',1,2,3,4,5,6,7,8,9,100]

n1, n2, n3, *outra_lista, n4 = lista

print(n1, n2)


#desempacotamento de lista pegando o ultimo valor
lista = ['Victor', 'Joao', 'Maria',1,2,3,4,5,6,7,8,9,100]

n1, n2, n3, *outra_lista, ultimo_valor = lista

print(ultimo_valor)

