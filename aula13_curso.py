'''For in em Python
Iterando strings com for
Função range(start=0, stop, step=1)'''


# acessando o indice da minha string com while
texto = 'python'
nova_string=''

c = 0
while c < len(texto):
    print(texto[c])
    c += 1


# acessando o indice da minha string com for
for letra in texto:
    print(letra)


# utilizando a função range
for n in range(10):
    print(n)


# utilizando a função range (decrementando)
for n in range(20,10,-1):
    print(n)


# utilizando a função range (multiplos)
for n in range(100):
    if n %8==0:
        print(n)

# utilizanndo funções .() em for (checando letra por letra)
for letra in texto:
    if letra == 't':         #a letra é t? não? entao pula
        nova_string = nova_string + letra.upper()
    elif letra == 'h':       #a letra é h? não? então pula
        nova_string += letra.upper()
    else:          #execute
        nova_string += letra
print(nova_string)