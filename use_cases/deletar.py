from repositorio import banco
from use_cases.buscar import buscaCodigo
from use_cases.adicionar import adicionarProduto

def deletarProduto(codigo: int):
    produto = buscaCodigo(codigo)
    if produto:
        banco.remove(produto) #.pop prejudicaria a sequência
        print('\nProduto removido com sucesso!')
    else:
        print('\nProduto não encontrado!')


if __name__ =="__main__": #dunder methods (teste de arquivos)
    adicionarProduto('Mouse','Periféricos',199.99)
    adicionarProduto('Monitor LG 29pol', 'Monitores', 599.99)
    adicionarProduto('RTX 570', 'Placa de vídeo', 899.99)
    print(buscaCodigo(2))
    print(buscaCodigo(5))
    print(banco)
    deletarProduto(1)
    print(banco)
    adicionarProduto('Mouse', 'Periféricos', 199.99)
    print(banco)

