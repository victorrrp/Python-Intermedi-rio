'''Interando strings com while em python'''

minha_string = 'o rato roeu a roupa do rei de roma'
tam_string=len(minha_string)

c = 0

nova_string = ''
while c < tam_string:
    
    if minha_string[c] == 'r':
        nova_string = nova_string + minha_string[c].upper()
    else:
        nova_string = nova_string + minha_string[c]

    c += 1

print(nova_string)