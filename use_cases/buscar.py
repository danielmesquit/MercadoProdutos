from repositorio import banco
from use_cases.adicionar import adicionarProduto

def buscaCodigo(codigo: int) -> dict or None:
    for produto in banco:
        if codigo == produto['codigo']:
            print(f'\n--O produto com o código {codigo} existe--')
            print(f"\nCódigo: {produto['codigo']}")
            print(f"Nome: {produto['nome']}")
            print(f"Categoria: {produto['categoria']}")
            print(f"Preço: {produto['preco']}")
            return produto

    print(f'\nNão há produto com o código {codigo} registrado.')
    return None



if __name__ =="__main__": #dunder methods (teste de arquivos)
    adicionarProduto('Mouse','Periféricos',199.99)
    adicionarProduto('Monitor LG 29pol', 'Monitores', 599.99)
    adicionarProduto('RTX 570', 'Placa de vídeo', 899.99)
    print(buscaCodigo(2))
    print(buscaCodigo(5))