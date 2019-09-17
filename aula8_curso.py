'''Formatando valores com modificadores
:s-Texto (strings)
:d-Inteiro
:f-Numeros de ponto flutuante(float)
:(numero)f-Quantidade de casas decimais(float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO-s, d, ou f)'''

#formata para string
nome0='Victor Pereira'
print(f'{nome0:s}')

#:(numero)f-Quantidade de casas decimais(float)
n1=10
n2=2
divisao=n1/n2

print(f'{divisao:.2f}') 
print("O resultado da divisão é:{:.2f}".format(divisao))

''':(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO-s, d, ou f) 
para determinar quantidade de caracteres na minha variavel'''

#acrescenta para esquerda
n3=30
print(f'{n3:0>10}')

#conta a partir das casas decimais ja existentes
n4=1150
print(f'{n4:0>10}')

#acrescenta para direita
n5=30
print(f'{n5:0<10}')

#coloca a variavel ao centro dos caracteres acrescentados
n6=30
print(f'{n6:0^10}')

#é possivel utilizar outros formatadores
n7=(30)
print(f'{n7:0<10.2f}')

#tambem funciona com palavras adicionando elementos
nome='Victor Pereira'
print(f'{nome:#^50}')

#buscando indice
nome1='Victor'
sobrenome='Pereira'
nome_formatado=f'{sobrenome}'
print(nome_formatado)