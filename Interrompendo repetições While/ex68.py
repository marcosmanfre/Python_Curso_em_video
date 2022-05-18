from random import randint
v = 0

while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    print('deu par' if total % 2 == 0 else 'Deu impar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você Perdeu! ')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você Venceu! ')
            v += 1
        else:
            print('Você Perdeu! ')
            break
    print('Vamos jogar novamente ...')
print(f'Game Over! você venceu {v} vez')
