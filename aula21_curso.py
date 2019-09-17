'''Funções - def em Python (parte 1)'''


#define uma função para facilitar na edição e manipulação do codigo
def função():
    print('Hello World')

função()
função()
função()
função()


#colocando variaveis na função
def saudação(msg, nome):
    print(msg, nome)


#função por função é possivel modificar o codigo
saudação('Pode pôr o que quiser', 'Victor')
saudação('oi', 'Pereira')
saudação('hello', 'da')
saudação('olá', 'Silva')


#colocando os valores dentro da função e alterando 
def valor(mensagem = 'Mensagem pré declarada na variavel'):
    print(mensagem)

valor()
valor('Valor alterado')