'''Listas em python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range'''

#concatenando listas atraves de variaveis
l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1 + l2

print(l1)
print(l2)
print(l3)


#utilizando .extend
l1 = [1,2,3]
l2 = [4,5,6]
l1.extend(l2)
print(l1)


#utilizando .extend modificando um valor
l2 = [4,5,6]
l1.extend('a')
print(l1)


#utilizando .append == incrementa um novo valor no final da lista
l2 = [4,5,6]
l2.append('b')
#buscando o novo valor no indice
print(l2[3])


#utilizando .insert == incrementa um novo valor em qualquer lugar na lista(utilize o indice)
l2 = [4,5,6]
l2.insert(0, 'banana')
#buscando o novo valor no indice
print(l2[0])


#utilizando o .pop == para deletar o ultimo indice
l2 = [4,5,6]
print(l2)
l2.pop()
print(l2)


#utilizando o del == para excluir (fatiamento)
l2 = [1,2,3,4,5,6,7,8,9]
del(l2[3:6])
print(l2)


#buscando o maior e menor valor da minha lista
print(max(l2))
print(min(l2))


#utilizando range (com list) para fazer uma lista (forma simples)
l2 =list(range(1,10))
print(l2)


#utilizando for para mostrar uma lista
for valor in l2:
    print(valor)


#utilizando for para mostrar uma lista e somar os valores
soma = 0
for valor in l2:
    soma += valor
print(soma)


#para saber os elementos da lista utilizando for
l2 = ['Victor', True, 10.5, 5]

for elemento in l2:
    print(f'O tipo de elemento é {type(elemento)} e seu valor é {elemento}')



#utilizando os comandos acima desenvolvimento de um mini jogo
secreto = 'perfume'
digitadas = []


while True:
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Digite apenas uma letra!')
        continue
    digitadas.append(letra)

    if letra in secreto:
        print(f'Letra correta!')
    else:
        print(f'Letra incorreta')
        digitadas.pop()
    
    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
            
    print(secreto_temporario)
            
    if secreto_temporario == secreto:
        print(f'Voce acertou! a palavra é {secreto}')
        break