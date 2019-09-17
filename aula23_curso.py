'''
1 - Crie uma função que exibe uma saudação com os parametros saudação e nome
'''

def função(saudação = 'Olá', nome = 'Victor'):
    print(saudação, nome)
    
função()

'''
2 - Crie uma função que receba 3 numeros como parametros e exiba soma entre eles.
'''

def soma(a,b,c):

    return a+b+c

somando = soma(1,1,1)  
print(somando)

'''
3 - Crie uma função que receba 2 numeros. O primeiro é um valor e o segundo um 
percentual (ex. 10%). Retorne (return) o valor do primeiro numero somado
do aumento do percentural do mesmo.
'''

def aumento_percentual(valor, percentual):
    return valor + (valor*percentual/100)

ap = aumento_percentual(50, 10)
print(ap)
ap = aumento_percentual(100, 10)
print(ap)
ap = aumento_percentual(10, 10)
print(ap)
ap = aumento_percentual(15,10)
print(ap)

'''
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne o fizz,
se o parâmetro da função for divisível por 5, retorne o buzz. Se o parâmetro da
função for divisível por 5 e por 3, reorne FizzBuzz, caso contrario, retorne o 
numero enviado
'''

def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    if n % 5 == 0:
        return 'Buzz'
    if n % 3 == 0:
        return 'Fizz'
    return n

print(fb(5))
print(fb(12))
print(fb(73))
print(fb(7))
print(fb(15))