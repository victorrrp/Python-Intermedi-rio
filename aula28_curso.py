'''
Tuplas em Python
A diferença da tupla pra lista é que não é possivel editar os elementos da tupla
'''

t_1 = (1,2,3, 'a', 'Victor Pereira')

print(t_1)#é possivel buscar o elemento da tupla da mesma forma que na lista, pelo índice

'''
Para criar uma tupla sem parênteses
deve-se colocar uma vírgula no final da variavel, senão ocorre erro
'''


#Desempacotando tuplas
t1 = 1,2,'Victor',4,5
t2 = 6,7,8,9,10
t3 = t1 + t2

n1, n2, n3, *_ = t3

print(t3)


#Repetindo o valor da tupla utilizando multiplicador
t4 = (1,2,'Victor', 4, 5)*20
print(t4)


#Convertendo tuplas em listas e buscando pelo indice
t5 = (1,2,3,4,5)
t5 = list(t5)

t5[1] = 3000
print(t5)