from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valores sorteado foi {max(numeros)}')
print(f'O menor valores sorteado foi {min(numeros)}')
