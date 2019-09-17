'''
List comprehension em python.
Com esse conceito, podemos otimizar a utilização de listas, sua criação e seu manuseio.
possibilitando diminuir algumas linhas de código.
'''


#iterando l1
l1 = [1,2,3,4,5,6,7,8,9]


#multiplicando cada elemento da lista por 2
ex1 = [v*2 for v in l1]
print(ex1)


#criando uma tupla para cada elemento
ex2 = [(v,v2)for v in l1 for v2 in range(3)]
print(ex2)


#substituindo letra na string (utilizando replace)
l2 = ['Victor', 'Mauro', 'Maria']
ex3 = [v.replace('a', '@').upper() for v in l2] #.upper - coloca as letras em maiusculas

print(ex3)


#trocando valores na iteração
tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2'),
)

ex4 = [(y, x) for x, y in tupla]
#transformando a tupla num dicionário
ex4 = dict(ex4)

print(ex4)


#filtrando uma lista para somente pares com for (if)
l3 = list(range(100))
ex5 = [v for v in l3 if v%2 == 0]
print(ex5)

#repetindo o código acima, porém acrescentando o else
l3 = list(range(100))
ex6 = [v if v%3 == 0 else 0 for v in l3]
print(ex6)

