'''Sets em python (conjuntos)
* add(adiciona), update(atualiza), clear(limpa), discard
* union [ | ] (une)
* intersection [ & ] (todos os elementos presentes nos dois sets)
* difference [ - ] (elementos apenas no set da esquerda)
* symmetric_difference [ ^ ] (elementos que estão nos dois sets, mas não em ambos)

A maior diferença entre os sets, listas e tuplas é que os sets só suportam elementos unicos
Não há como acessar um valor específico num set pois o mesmo não tem índice
'''

#set (modo normal)
s1 = {1,2,3,4,5}
print(type(s1))

'''
para efeito de comparação

#tupla
t1 = (1,2,3,4,5)
print(type(t1))


#dicionário
d1 = {'1':'2'}
print(type(d1))
'''

#para criar um set vazio
s1 = set()

#para adicionar valor(add)
s1.add(1)
s1.add(2)
s1.add(3)

#para descartar valor(discard)
s1.discard(3)


#geralmente usa-se sets para eliminar elementos duplicados. ex.:
#pode acontecer de seus elementos voltarem fora de ordem

l1 = [1,1,'Victor',1,2,2,3,6,6,5,4,4,4,5,8, 'Victor', 'Victor']

l1 = set(l1)
l1 = list(l1)

print(l1)


#union no set (mostra todos os elementos excluindo os repetidos. ex.:)
s1 = {1,2,3,4,5}
s2 = {1,2,3,4,5,6}

s3 = s1|s2

print(s3)


#intersection no set (mostra todos os elementos presentes no set. o elemento 
#que estiver em apenas um dos sets, é automaticamente eliminado. ex.:)
s1 = {1,2,3,4,5}
s2 = {1,2,3,4,5,6}
s3 = s1 & s2

print(s3)


#difference (mostra somente os elementos únicos no set da esquerda. ex.:)
s1 = {1,2,3,4,5,16,15}
s2 = {1,2,3,4,5,6}
s3 = s1 - s2

print(s3)


#symmetric difference no set (mostra somente os elementos unicos nos dois sets em questão. ex.:)
s1 = {1,2,3,4,5,7,9,11}
s2 = {1,2,3,4,5,6,8,10}
s3 = s1 ^ s2

print(s3)

#fazendo cast com set

l1 = ['Victor', 'Pereira', 'Silva']
l2 = ['Luiz', 'Maria', 'Joao', 'Joao', 'Joao', 'Joao', 'Joao', 'Luiz', 'Joao', 'Joao', 'Joao']

if set(l1) == set(l2):
    print('L1 é igual a L2')
else:
    print('L1 é diferente de L2')