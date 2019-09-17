nome=input("Digite seu nome: ")
idade=int(input("Digite sua idade: "))
ano_atual=int(input("Digite o ano atual: "))
altura=float(input("Digite sua altura em metros: "))
peso=float(input("Digite seu peso: "))

ano_nascimento=ano_atual-idade
imc=peso/(altura*altura)

print("seu nome é:{}".format(nome))
print("sua idade é:{}".format(idade))
print("o ano atual é:{}".format(ano_atual))
print("sua altura é:{}".format(altura))
print("seu peso é:{}".format(peso))
print("seu ano de nascimento é:{}".format(ano_nascimento))
print("seu IMC é:{:.2f}".format(imc))