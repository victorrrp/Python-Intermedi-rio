'''
Módulos padrão em Python
*Módulos são arquivos .py e servem para estender as funcionalidades padrão da linguagem
'''

#mostrando qual plataforma que o python 
#está sendo executado através de um módulo
import sys
print(sys.platform) #depois do ponto pode-se verificar todos os recursos disponiveis no módulo

import random
print(random.randint(0, 10))


#outra maneira. uma vez declarado o recurso, 
#não há como verificar os recursos no print
from sys import platform
print(platform)


from random import randint, random #é possivel importar mais de um recurso no mesmo módulo
