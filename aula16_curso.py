'''
*Split - Dividir uma string gerando uma lista
*Join - Juntar uma lista
*Enumerate - Enumerar elementos da lista
'''
# utilizando a função split
string = 'Voce pensa q o Flamengo é time? o Flamengo n é time n n n'
lista_1 = string.split(' ')
lista_2 = string.split(',')
print(lista_1)
print(lista_2)

# utilizando a funço split dentro do for
for valor in lista_1:
    print(f'A palavra "{valor}" apareceu {lista_1.count(valor)}x na frase')


palavra = ''
contagem = 0

for valor in lista_1:
    qtd_vezes = lista_1.count(valor)
    
    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor
print(f'A palavra que apareceu mais vezes é: {palavra}({contagem}x)')