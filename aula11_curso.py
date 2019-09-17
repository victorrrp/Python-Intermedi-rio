'''while / else
contadores
acumuladores'''

contador = 1
acumulador = 1

while contador <= 50:
    print(contador, acumulador)

    acumulador = acumulador + contador
    contador += 1
else:
    print('Fim de programa')