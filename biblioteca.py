from livro import Livro

livro1 = Livro("O Código Da Vinci", " Dan Brown", 2003)
livro2 = Livro("Orgulho e Preconceito", "Jane Austen", 1813)
livro3 = Livro("Brave New World", "Aldous Huxley", 1932)
livro4 = Livro("Another Book from 1949", "Another Author", 1949)

livro2.emprestar()

print(f"Disponível após emprestar '{livro2.titulo}': {livro2.disponivel}")

livros_disponiveis_1949 = Livro.verificar_disponibilidade(1949)
print("Livros disponíveis publicados em 1949:")
for livro in livros_disponiveis_1949:
    print(livro)