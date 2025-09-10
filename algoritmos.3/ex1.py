#1)

Aluno={
    'nome': 'Paulo',
    'idade': '23',
    'curso': 'ESW'
}
print(Aluno['nome'])

Aluno['nota']= 9.5
del Aluno['idade']
print('aluno')

if 'curso' in Aluno:
    print('A chave "curso" existe!')
else:
    print('A chave "curso" não existe')
