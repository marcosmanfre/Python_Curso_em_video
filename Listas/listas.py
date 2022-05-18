'''num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
#num.sort()
#num.sort(reverse=True)
num.insert(2, 2)
num.pop(2)
print(num)
print(f'Essa lista tem {len(num)} elementos. ')'''

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'posição {c} o valor {v} ...')


valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'posição {c} o valor {v} ...')