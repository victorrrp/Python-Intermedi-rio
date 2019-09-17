'''
Try, Except - Tratando exceções em python
Exceções são erros que pararão seu programa
try, except funciona basicamente como if/else
'''

#o try executa o código verificando erros, caso tenha, ele pula para except e continua o codigo
#é reomendado excutar o código, ver o nome do erro e utiliza-lo para não ficar muito amplo. ex.:
try:
    print(a)
except (NameError, KeyError) as erro:    #é possivel fazer tuplas
    print('Erro do desenvolvedor, fale com ele.')

except Exception as erro:    #é possível utilizar mais de um except no mesmo código
    print('Erro desconhecido')

else:   #será executado no bloco toda vez que não houver exceção (0 erro)
    print('Seu código foi executado com sucesso!')

finally:   #diferentemente do else, o finally será executado com ou sem erro
    print('Finalmente.')

print('Vamos continuar...')
