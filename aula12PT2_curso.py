'''manipulando strings com while em python pt2'''
'''utilizando contador para saber qual letra 
aparece mais e quantas vezes aparece'''


minha_string = 'o rato roeu a roupa do rei de roma'
tam_string = len(minha_string)

c = 0
contagem = 0
letra = ''
while c < tam_string:
    conta = minha_string.count(minha_string[c])

    if contagem < conta and minha_string[c].strip():
        letra = minha_string[c]
        contagem = conta


    c += 1

print(letra, contagem)