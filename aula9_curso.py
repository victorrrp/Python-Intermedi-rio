'''Manipulando strings
* String indices
* Fatiamento de strings
* Funçoes built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.'''

#indices positivos    [012345678]
texto=                'Python s2'
#indices negativos   -[987654321]

print(texto[2]) #buscando o indice
print(texto[:5]) #fatiamento
print(texto[-2]) #utilizando os indices negativos
print(texto[0:5:2]) #pulando os indices da string [inicio:sim:tam passo]
print(len(texto)) #tamanho total da string

'''para pegar o primeiro caracter utilize o indice 0]
para pegar o ultimo, utilize -1'''