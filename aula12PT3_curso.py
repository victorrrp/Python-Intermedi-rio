'''manipulando strings com while em python pt2'''
'''utilizando contador e o input com o usuário'''

while True:

    minha_string = input("Digite uma frase: ")
    tam_string = len(minha_string)

    c = 0
    contagem = 0
    letra = ''
    while c < tam_string:
        conta = minha_string.count(minha_string[c])

        if contagem < conta and minha_string[c].strip(): #remove os espaços no inicio e no final da string
            letra = minha_string[c]
            contagem = conta


        c += 1

    print(letra, contagem)