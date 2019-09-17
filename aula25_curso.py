'''
Funções (def) em python
Uma vez que a variavel global foi declarada, não é possível modificá-la dentro do escopo
'''
variavel = 'valor'

def func():
    print(variavel)

def func2():
    variavel = 'Outro valor' #essa variavel em questão não é mesma no inicio do programa pois foi criada dentro do escopo do def
    print(variavel)

func()
func2()

print(variavel)

'''
para mudar uma variavel global dentro do escopo, 
utilize o comando "global" antes da sua variavel

ex.:

def func2():
    global variavel
    variavel = 'Outro valor'
    print(variavel)
'''

#modificando a variavel dentro do escopo
var1 = 'valor'

def func1():
    outra_variavel = 'valor'
    return outra_variavel

def func3(arg):
    print(arg)

var = func1()
func3(var1)