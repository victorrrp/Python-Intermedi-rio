'''
Count - Itertools
*Função que gera um contador que retorna um iterador

O python já tem um contador próprio, basta colocar 
duas linhas de código: from itertools import count
'''

from itertools import count

contador = count()

#iterador (pode-se colocar quantos quiser, pois é um iterador)
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))


#como é um iterador, o for pede o proximo valor e o contador obedece e cai no laço infinito
for valor in contador: 
    print(valor)


#para parar o contador pode-se usar o if como limitador
    if valor >=10:
        break


#é possível dar um inicio ao contador pré determinando um valor
contador = count(start=5)

for valor in contador:
    print(valor)

    if valor >= 10:
        break


#pode-se usar o step para determinar de quanto em quanto pulará a contagem
contador = count(start=10, step=1) #é possivel utilizar o step de forma negativa. ex.: (start = 9, step = -1)

for valor in contador:
    print(valor)

    if valor >= 10:
        break


