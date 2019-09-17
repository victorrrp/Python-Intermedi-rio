'''
Uso de Try e Except como condicional
'''

#utilizando codigo errado e corrigindo com try, except:
numero = float(input('Digite um número: '))
print(numero*5)


#corrigindo. fazendo conversão para inteiro
def converte_numero1(valor):
    try:
        valor = int(valor)
        return (valor)
    except ValueError:
        pass

numero = converte_numero1(input('Digite um numero: '))
print(numero * 5)


#fazendo conversão para float
def converte_numero2(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass

numero = converte_numero2(input('Digite um numero: '))
print(numero * 5)


#fazendo conversão para caracter
def converte_numero3(valor):
    try:
        valor = int(valor)
        return valor #se não tiver algum erro, retornar número. Caso contrário 'cair' no except
    except ValueError:
        try:
            valor = float(valor)
            return valor #se não tiver algum erro, retornar número. Caso contrário 'cair' no except
        except ValueError: 
            pass

while True:
    numero = converte_numero3(input('Digite um numero: '))
    
    if numero is None:
        print('Erro: isso não é um numero')
    else:
        print(numero*2)