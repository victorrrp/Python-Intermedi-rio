'''
Sistema simples de perguntas e respostas com dicionários em python
'''

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2?',
        'respostas': {
            'a':'1',
            'b':'2',
            'c':'3',
            'd':'4',
        },
        'resposta_certa': 'd',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 5*5',
        'respostas': {
            'a':'10',
            'b':'15',
            'c':'20',
            'd':'25',
        },
        'resposta_certa':'d',
    }
}
print()

respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == pv['resposta_certa']:
        print('Parabéns, você acertou!!!!!!')
        respostas_certas += 1
    else:
        print('Ah, não! Você errou :(')

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas/qtd_perguntas*100

print(f'Você acertou {respostas_certas} perguntas e sua porcentagem de acerto foi de {porcentagem_acerto}%')