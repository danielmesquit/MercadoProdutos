from repositorio import banco

codigo = 0

def gerarProduto(nome,categoria,preco):

    #autoriza a função a manipular variável fora do escopo
    global codigo
    codigo += 1
    produto = {
        'codigo': codigo,
        'nome': nome,
        'categoria': categoria,
        'preco': preco
    }
    return produto

def adicionarProduto(nome,categoria,preco):
    codigo

    produto = gerarProduto(nome,categoria,preco)
    banco.append(produto)

    # nomeProduto = banco[codigo-1]['nome']  #reduzir 1 para coletar a posição correta
    #Erro ao deletar qualquer posição
    # print(f'O produto {nomeProduto} foi adicionado com sucesso!')

    print(f'O produto foi adicionado com sucesso!')


if __name__ =="__main__": #dunder methods (teste de arquivos)
    adicionarProduto('Mouse','Periféricos',199.99)
    print(banco)