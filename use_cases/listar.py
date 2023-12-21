from repositorio import banco
from use_cases.adicionar import adicionarProduto

def listarProdutos():
    print('--Lista de Produtos--')

    for produto in banco:
        print(f"\nCódigo: {produto['codigo']}")
        print(f"Nome: {produto['nome']}")
        print(f"Categoria: {produto['categoria']}")
        print(f"Preço: {produto['preco']}")

if __name__ =="__main__": #dunder methods (teste de arquivos)
    adicionarProduto('Mouse','Periféricos',199.99)
    adicionarProduto('Monitor LG 29pol', 'Monitores', 599.99)
    adicionarProduto('RTX 570', 'Placa de vídeo', 899.99)
    listarProdutos()
