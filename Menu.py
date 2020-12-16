from FunçõesFilme import *
from FunçõesSala import *
#  from FunçõesSessões import *
#  from FunçõesRelatórios import *


def Menu():
    BDSESSAO = {}
    BDFILMES = {}
    BDSALAS = {}

    opcao = 0
    while opcao != 5:  # Menu Inicial
        print("\n1 - Submenu de Salas")
        print("2 - Submenu de Filmes")
        print("3 - Submenu de Sessões")
        print("4 - Submenu Relatórios")
        print("5 - Sair")
        opcao = int(input("\nDigite a opcao desejada: "))
        while opcao < 1 or opcao > 5:
            print("Opcao invalida!")
            opcao = int(input("\nDigite a opcao desejada: "))

        if opcao == 1:  # Submenu Salas
            while opcao != 5:
                print("\n1 - Listar Salas")
                print("2 - Listar um Elemento da Sala")
                print("3 - Incluir Sala")
                print("4 - Alterar ou Excluir informação da Sala")
                print("5 - Voltar para o Menu Inicial")

                opcao = int(input("\nDigite a opcao desejada: "))
                while opcao < 1 or opcao > 5:
                    print("Opcao invalida!")
                    opcao = int(input("\nDigite a opcao desejada: "))

                if opcao == 1:
                    ListaTodasSalas(BDSALAS)
                elif opcao == 2:
                    ListarElementoLista(BDSALAS)
                elif opcao == 3:
                    IncluirSala(BDSALAS)
                    print(BDSALAS)
                elif opcao == 4:
                    AlterarOuExcluirSalas(BDSALAS)
                    print(BDSALAS)
                elif opcao == 5:
                    Menu()
        elif opcao == 2:  # Submenu Filmes
            while opcao != 5:
                print("\n1 - Listar Filmes:")
                print("2 - Listar um Elemento do Filme:")
                print("3 - Incluir Filme:")
                print("4 - Alterar ou Excluir informação da Filme:")
                print("5 - Voltar para o Menu Inicial:")

                opcao = int(input("\nDigite a opcao desejada: "))
                while opcao < 1 or opcao > 5:
                    print("\nOpcao invalida!")
                    opcao = int(input("\nDigite a opcao desejada: "))

                if opcao == 1:
                    ListarTodosFilmes(BDFILMES)
                elif opcao == 2:
                    ListarElementoFilme(BDFILMES)
                elif opcao == 3:
                    # inserindo a lista de filmes na lista BDFILMES:
                    IncluirFilmes(BDFILMES)
                elif opcao == 4:
                    AlterarOuExcluirFilmes(BDFILMES)
                elif opcao == 5:
                    Menu()
        elif opcao == 3: # Submenu Sessões
            while opcao != 5:
                print("1 - Listar Sessões")
                print("2 - Listar um Elemento de uma Sessão")
                print("3 - Incluir Sessao")
                print("4 - Alterar ou Excluir informação de uma Sessões")

                opcao = int(input("Digite a opcao desejada: "))
                while opcao < 1 or opcao > 4:
                    print("Opcao invalida!")
                    opcao = int(input("Digite a opcao desejada: "))
                    if opcao == 1:
                        print(BDSESSAO)
                    elif opcao == 2:
                        print("Teste")
                    elif opcao == 3:
                        print("Teste")
                    elif opcao == 4:
                        print("Teste")
        elif opcao == 4:
            print("sad")
        elif opcao == 5:
            print("** programa finalizado **")
            break


"""

estou corrigindo a passagem de parametros entre as funções e arrumando o menu principal em uma função separada. ok
preciso fazer salvar os dados em dicionário e colocar como chave o código e valor usar lista ou tupla dependendo do que 
for armazenar. ok
preciso achar o pq não está achando o dado pedido pelo usuario no dicionario.

"""