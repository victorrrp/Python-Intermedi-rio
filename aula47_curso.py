'''
Como criar módulos em python
'''
import math

PI = math.pi

#Modo normal utilizando list comprehension
def dobra_lista(lista):
    return [x * 2 for x in lista]


#utilizando uma função que multiplica
def multiplica(lista):
    r = 1
    for i in lista:
        r*= i
    return r


#para não aparecer todo o código quando for executado no módulo, faça o seguinte:
if __name__ == '__main__':
    lista = [1,2,3,4,5]
    print(dobra_lista(lista))
    print(multiplica(lista))
    print(PI)
