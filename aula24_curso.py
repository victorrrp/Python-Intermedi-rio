'''
Funções (def) em python - *args **kwargs - Pt3
Args - Arguments
Kwargs - Key Words Arguments
'''

def func_0(a1, a2, a3, a4, a5, nome=None, a6=None): #a partir do momento em q um valor for nomeado, todos os seguintes tem que ser nomeados também
    print(a1, a2, a3, a4, a5, nome, a6)
    return nome, a6

var = func_0(1,2,3,4,5, nome='Victor', a6='5')
print(var) #pode-se acessar o argumento pelo índice, sendo: [1] Victor; [2] 5

#utilizando *args - espécie de empacotamento e desempacotamento (correlação com aula17)

def func1(*args):
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))

func1(1,2,3,4,5)

#convertendo tuplas para listas com cast

def func2(*args):
    args = list(args)
    args[0] = 20
    print(args)

func2(1,2,3,4,5)

#utilizando for

def func3(*args):
    for v in args:
        print(v)

func3(1,2,3,4,5)

def func4(*args):
    print(args)

lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]

#desempacotando duas listas ao mesmo tempo. caso prefira manter empacotada, retire o *.
func4(*lista, *lista2) 
#ex.: func4(*lista, lista2)

def func5(*args, **kwargs):
    print(args)
    
    idade = kwargs['idade'] #mostra na tela os argumentos especificados(pedidos)
    print(idade) 

lista = [1,2,3,4,5]
lista3 = [10,20,30,40,50]
func5(*lista, *lista3, nome='Victor', sobrenome='Pereira', idade=22)