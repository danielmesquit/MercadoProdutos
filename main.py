from use_cases.adicionar import adicionarProduto
from use_cases.buscar import buscaCodigo
from use_cases.deletar import deletarProduto
from use_cases.listar import listarProdutos
from use_cases.editar import editarProduto

def menu():

    while True:
        print('-----Menu-----\n')
        print('----- 1 para Adicionar Produtos -----')
        print('----- 2 para Buscar Produtos -----')
        print('----- 3 para Listar Produtos -----')
        print('----- 4 para Deletar Produtos -----')
        print('----- 5 para Editar Produtos -----')

        opcao = int(input('Digite a opção escolhida: '))

        if opcao == 1 :
            nome = input('Digite o nome do produto: ')
            categoria = input('Digite a categoria do produto:')
            preco = float(input('Digite o preço do produto: '))
            adicionarProduto(nome,categoria,preco)

        elif opcao == 2:
            codigo = int(input('Digite o código do produto:'))
            buscaCodigo(codigo)

        elif opcao == 3:
            listarProdutos()

        elif opcao == 4:
            codigo = int(input('Digite o código do produto que deseja excluir: '))
            deletarProduto(codigo)

        elif opcao == 5 :
            codigo = int(input('Digite o código do produto:'))
            nome = input('Digite o nome do novo produto: ')
            categoria = input('Digite a categoria do novo produto:')
            preco = float(input('Digite o preço do novo produto: '))
            editarProduto(codigo, nome,categoria, preco)

        else:
            break

menu()