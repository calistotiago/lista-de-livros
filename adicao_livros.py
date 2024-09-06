#adicionar livros em lista
meus_livros = {'Nome' : 'Dom Casmurro',
               'Autor' : 'Machado de Assis',
               'Ano' : '1899'}

print(meus_livros)

for i in range(1):
    nome = input('Digite o nome do Livro : ')
    meus_livros['Nome'] = nome
    autor = input('DIgite nome do autor : ')
    meus_livros['Autor'] = autor
    ano = int(input('Ano de Publicação do livro : '))
    meus_livros['Ano'] = ano

print(meus_livros['Nome'])
print(meus_livros['Autor'])
print(meus_livros['Ano'])

