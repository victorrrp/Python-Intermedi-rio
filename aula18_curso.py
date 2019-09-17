'''Trocando o valor entre variáveis'''

#em modo normal é:

x = 10
y = 'Victor'

z = x
x = y
y = z

print(f'x={x} e y={y}')

#em python a inversão de valores fica da seguinte forma

x = 10
y = 'Victor'

x, y = y, x
print(f'x={x} e y={y}')


#inversao com mais variaveis
x = 10
y = 'Victor'
z = 'Pereira'

x, y, z = z, x, y
print(f'x={x} e y={y} e z={z}')