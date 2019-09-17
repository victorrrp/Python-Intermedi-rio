'''Operador ternario em python'''


#forma comum booleana
logged_user = True

if logged_user:
    msg = 'Usuário logado.'
else:
    msg = 'Usuário precisa logar.'

print(msg)

#utilizando operador ternario
logged_user = True

msg = 'Usuário logado.' if logged_user else 'Usuário precisa logar.'

print(msg)


#outras situações
idade = input("Qual sua idade? ")

if not idade.isnumeric(): #forma de limitar a variavel para aceitar (no caso) somente numeros
    print('apenas numeros sao permitidos')
else:
    idade = int(idade)
    eh_maior = (idade >= 18)
    msg = 'Pode acessar' if eh_maior else 'Não pode acessar.'

    print (msg)