'''
Lançando suas próprias exceções
'''

#forma de 'logar' o erro
def divide(n1, n2):
    try:
        return n1/n2
    except ZeroDivisionError as erro:
        print(erro)
        return False

print(divide(2,0))


#Outro comportamento 'logando' o erro
def divide1(n1, n2):
    try:
        return n1/n2
    except ZeroDivisionError as erro:
        print(erro)
        return False

try:
    print(divide(2,0))
except:
    print('erro')


#capturando a exceção num arquivo de log, ou numa base de dados e re-lançando a mesma exceção
def divide2(n1, n2):
    try:
        return n1/n2
    except ZeroDivisionError as erro:
        print('Log: ', erro)
        raise #tem como finalidade invocar uma Exception no momento oportuno.

try:
    print(divide2(2,0))
except ZeroDivisionError as erro: #capturando...
    print('erro')


#lançando sua própria exceção
def divide3(n1, n2):
    if n2 == 0:
        raise ValueError('n2 não pode ser 0.')#nessa etapa é necessário ser bem específico quanto ao erro
    return n1 / n2

print(divide3(2,0))

