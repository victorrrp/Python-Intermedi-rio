'''While em python'''

x=0
while x<10: #enquanto
    if x==3:
        x+=1
        continue #pula para o próximo laço (ele para de executar o trecho de cod)
    print(x)
    x=x+1

print("Acabou!")


y=0
while y<10:
    if y==3:
        y+=1
        break #para parar de executar o laço
    print(y)
    y=y+1   
print("Acabou!")

a = 0 # coluna

while a < 10:
    b = 0 # linha
    while b < 5:
        print(f'({a},{b})')
        b += 1
    a += 1

while True:
    num1=input("Digite um numero: ")
    operador=input("Informe o operador: ")
    num2=input("Digite outro numero: ")
    sair=input("Deseja sair? s/n: ")

    if sair == 's':
        break

    if not num1.isnumeric() or not num2.isnumeric():
        print('Voce precisa digitar um numero.')
        continue
    
    #cast
    num1 = int(num1)
    num2 = int(num2)

    if operador == '+':
        print(num1 + num2)
    elif operador == '-':
        print(num1 - num2)
    elif operador == '*':
        print(num1 * num2)
    elif operador == '/':
        print(num1 / num2)
    else:
        print("Operação invalida")
