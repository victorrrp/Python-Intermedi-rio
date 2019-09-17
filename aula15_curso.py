'''For / Else em python'''

variavel = ['a', 'b', 'c']

for valor in variavel:
    if valor.startswith('J'):#checa se a string começa com determinada letra
        print('Começa com J') 
    else:
        print('Não começa com J')

comeca_com_j = False
for valor in variavel:
    if valor.startswith('J'):
        comeca_com_j = True

if comeca_com_j:
    print('Existe uma palavra que começa com J')
else:
    print('Não tem nenhuma palavra que começa com J')