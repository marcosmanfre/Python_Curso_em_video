'''dados = {'nome': 'Pedro', 'idade':25}

print(dados)
dados['sexo'] = 'M'
print(dados)'''

filme = {'Titulo': 'Star Wars',
       'Ano': 1977,
       'Diretor': 'George Lucas'        
        }

print(filme)
print(filme.values())
print(filme.keys())
print(filme.items())

for k, v in filme.items():
    print(f'O {k} é {v}')