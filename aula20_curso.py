'''Expressão condicional com operador OR'''


#modo normal
nome = input('Digite seu nome: ')

if nome:
    print(nome)
else:
    print('Voce nao digitou nada.')



#utilizando OR
nome = input('Digite seu nome: ')
print(nome or 'Voce nao digitou nada')

#OR pega o primeiro valor True na sequencia de variaveis

a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'Victor'

variavel = a or b or c or d or e or f or g
print(variavel)