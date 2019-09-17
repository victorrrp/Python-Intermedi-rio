'''Faça um programa que peça ao usuário para digitar um numero inteiro.
Informe se este numero é par ou impar. Caso o usuário não digite um numero
informe que nao é um numero inteiro.'''

num=input('digite um numero inteiro: ')

if num.isdigit():
    num=int(num)
    if num%2==0:
        print('este numero é par')
    elif num%2==1:
        print('este numero é impar')
else:
    print('Isso nao é um numero')


'''Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito,
exiba a saudação apropriada. Ex. "Bom dia0-11, Boa tarde 12-17 e Boa noite18-23.'''

hora=(input("informe a hora(0-23): "))

if hora.isdigit():
    hora=int(hora)

    if hora<0 or hora>23:
        print("Horario deve estar entre 0 e 23")

    if hora <=11:
        print("Bom dia!")
    elif hora <=17:
        print("Boa tarde!")
    else:
        print("Boa noite!")

'''Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 7, escreva
"Seu nome é normal"; se for maior que 6 escreva "Seu nome é muito grande".'''

nome=input("Digite seu primeiro nome: ")

tamanho = len(nome)


if tamanho<=4:
    print("Seu nome é curto")
elif tamanho<=6:
    print("Seu nome é normal")
else:
    print("Seu nome é grande")