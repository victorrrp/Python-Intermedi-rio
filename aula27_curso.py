'''Funções anônimas ou Expressões lambda'''

#modo normal de utilizar def para fazer operações mat
def funcao(arg, arg2):
    return arg*arg2

mult = funcao(5,5)
print(mult)

#utilizando lambda
a = lambda x, y: x * y

print(a(5,5))


#ordenando lista (modo normal)
lista = [
    ['p1', 13],
    ['p2', 23],
    ['p3', 15],
    ['p4', 5],
    ['p5', 30],
]

def func(item):
    return item[1]

lista.sort(key = func, reverse = True) #a utilização do reverse serve para inverter a ordem da lista
print(lista)


#utilizando lambda
lista = [
    ['p1', 13],
    ['p2', 23],
    ['p3', 15],
    ['p4', 5],
    ['p5', 30],
]

lista.sort(key =lambda i: i[1])
print(lista)

'''
também é possivel fazer com sorted. ficaria assim:

print(sorted(lista, key = lambda i: i[1]))
print(lista)
'''