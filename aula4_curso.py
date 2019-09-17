'''entrada de dados'''
nome=input("Qual seu nome: ")
idade=input("Qual sua idade: ")

ano_nascimento=2019-int(idade)


#f'string-> simplifica a declaração de variaveis no print
print(f'{nome} tem {idade}. '
      f'{nome} nasceu em {ano_nascimento}.')