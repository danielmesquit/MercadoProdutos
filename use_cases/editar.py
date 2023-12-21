from repositorio import banco
from use_cases.buscar import buscaCodigo
from use_cases.adicionar import adicionarProduto

def editarProduto(codigo, nome, categoria, preco):
    produto = buscaCodigo(codigo)
    if produto:
        produto['nome'] = nome
        produto['categoria'] = categoria
        produto['preco'] = preco
        print('\nDados alterados com sucesso!\n'
              'Novo produto:')

        print(f"\nCódigo: {produto['codigo']}")
        print(f"Nome: {produto['nome']}")
        print(f"Categoria: {produto['categoria']}")
        print(f"Preço: {produto['preco']}")

    else:
        print('Produto não encontrado!')


if __name__ =="__main__": #dunder methods (teste de arquivos)
    adicionarProduto('Mouse','Periféricos',199.99)
    adicionarProduto('Monitor LG 29pol', 'Monitores', 599.99)
    adicionarProduto('RTX 570', 'Placa de vídeo', 899.99)
    editarProduto(2,'Teclado Mecânico Brown Swicth','Periféricos',200.00)