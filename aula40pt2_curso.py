#importando dados de outro arquivo para continuação do projeto
#é importante saber que muitas vezes você precisa mapear (alterar) os dados


from aula40_curso import produtos, pessoas, lista

#chamando uma função (map). é um pouco diferente pois ela chama outra função, no caso 'lambda'
nova_lista = map(lambda x: x*2, lista)


#para imprimir esse iteravel (nova_lista), é necessário chamar uma lista com typecast (list)
print(list(nova_lista))
print()


#fazendo o mesmo processo só que com list comprehension (simplificando o processo)
nova_lista = [x*2 for x in lista]
print(nova_lista)


#trabalhando a função map com dicionários 
#acessando o dicionário e pegando a coluna 'preço'
preços = map(lambda p: p['preço'], produtos)

for preço in preços:
    print(preço)

    
#a função lambda só funciona com expressões
#para alterar somente o preço sem modificar a estrutura do dicionário 

#a função aumenta_preço receberá um produto(p) e aumentará em 5% o preço dos produtos
def aumenta_preço(p):
    p['preço'] = round(p['preço']*1.05, 2)
    return p

novos_produtos = map(aumenta_preço, produtos)

for produto in novos_produtos:
    print(produto)


#para imprimir somente um certo tipo de valor faz-se o seguinte:
#caso queira a idade, troque o valor que está dentro da lambda
nomes = map(lambda p: p['nome'], pessoas)

for pessoa in nomes:
    print(pessoa)
