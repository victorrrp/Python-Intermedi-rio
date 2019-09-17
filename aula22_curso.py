'''Funções (def) em Python - return - Pt2'''
'''Uma função pode retornar qualquer coisa em Python'''

def função(var):
    print(var) #normalmente não se utiliza print em funções

função('Valor que eu quero')


def funcao(var):
    return var #se não colocar o return, a função nao retorna e da erro 

variavel = funcao('Valor que eu quero')

#o if else só seria executado caso nao tivesse o return
if variavel:
    print(variavel)
else:
    ('Nenhum valor')


#divisão em def (funções)
def divisao(n1, n2):
    return n1/n2
 
divide = divisao(8,2)
print(divide)


#variando comandos dentro das funções
#quando o Python encontra o "return" ele retorna o valor e não executa mais nada

def operacao(n1, n2):
    if n2 == 0:
        return 
    
    return n1/n2  #execuatando saindo do bloco if

divide = operacao(8,0)

if divide:
    print(divide)
else:
    print('Conta invalida.')


#retornando valores
def dumb():
    return [1, 2, 3] #se o return estiver vazio, ele retorna 'None' (não valor)

var = dumb()
print(var, type(var))