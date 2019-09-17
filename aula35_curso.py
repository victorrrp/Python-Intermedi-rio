'''
Geradores - São utilizados para otimizar o programa auxiliando na performance até mesmo da memória

Iteradores -  É um objeto que itera sobre outros

Iteráveis - É um objeto que pode-se iterar sobre ele, mas ele não é necessariamente um iterador

'''
#exemplo de geradores

#maneira normal
def gera():
    variavel = 'Valor 1'
    yield variavel
    variavel = 'Valor 2'
    yield variavel
    variavel = 'Valor 3'
    yield variavel

g =  gera()

print(next(g))  
print(next(g)) 
print(next(g))


#melhor maneira
def gera1():
    variavel = 'Valor 1'
    yield variavel
    variavel = 'Valor 2'
    yield variavel
    variavel = 'Valor 3'
    yield variavel

g =  gera1()

for v in g: #for é um exemplo de iterador
    print(v)

#EXEMPLOS!!!!

lista = [x for x in range(1000)]
print(type(lista))
lista = (x for x in range(1000))
print(type(lista))


l1 = (x for x in range(100))
for v in l1:
    print(v)