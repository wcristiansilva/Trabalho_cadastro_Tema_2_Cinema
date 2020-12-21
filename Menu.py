from FunçõesFilme import *
from FunçõesSala import *
from FunçõesSessões import *
#  from FunçõesRelatórios import *


def Menu():
    # Declaração de Dicionários
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
        opcao = int(input("\n Digite a opcao desejada: "))
        while opcao < 1 or opcao > 5:
            print("\n Opcao invalida!")
            opcao = int(input("\n Digite a opcao desejada: "))

        if opcao == 1:  # Submenu Salas
            while opcao != 5:
                print("\n1 - Listar Salas")
                print("2 - Listar uma Sala do Cadastro")
                print("3 - Incluir Sala")
                print("4 - Alterar ou Excluir informação da Sala")
                print("5 - Voltar para o Menu Inicial")

                opcao = int(input("\n Digite a opcao desejada: "))
                while opcao < 1 or opcao > 5:
                    print("\n Opcao invalida!")
                    opcao = int(input("\n Digite a opcao desejada: "))

                if opcao == 1:
                    ListaTodasSalas(BDSALAS)
                elif opcao == 2:
                    ListaUmaSalaDici(BDSALAS)
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
                    ListaUmFilmeDici(BDFILMES)
                elif opcao == 3:
                    # inserindo a lista de filmes na lista BDFILMES:
                    IncluirFilmes(BDFILMES)
                elif opcao == 4:
                    AlterarOuExcluirFilmes(BDFILMES)
                elif opcao == 5:
                    Menu()
        elif opcao == 3: # Submenu Sessões
            while opcao != 5:
                print("\n1 - Listar Sessões")
                print("2 - Listar um Elemento de uma Sessão")
                print("3 - Incluir Sessao")
                print("4 - Alterar ou Excluir informação de uma Sessões")
                print("5 - Voltar ao menu Principal")

                opcao = int(input("\nDigite a opcao desejada: "))

                while opcao < 1 or opcao > 5:
                    print("\nOpcao invalida!")
                    opcao = int(input("\nDigite a opcao desejada: "))

                if opcao == 1:
                    ListarTodasSessoes(BDSESSAO)
                elif opcao == 2:
                    ListarUmaSessaoDici(BDSESSAO)
                elif opcao == 3:
                    IncluirSessao(BDSESSAO, BDSALAS, BDFILMES)
                elif opcao == 4:
                    AlterarOuExcluirSessoes(BDSESSAO)
                elif opcao == 5:
                    Menu()
        elif opcao == 4:  #Submenu Relatórios
            print("sad")
        elif opcao == 5:  #Submenu Finalizar Programa
            print("\n** programa finalizado **\n\n")
            break


"""

estou corrigindo a passagem de parametros entre as funções e arrumando o menu principal em uma função separada. ok
preciso fazer salvar os dados em dicionário e colocar como chave o código e valor usar lista ou tupla dependendo do que 
for armazenar. ok
preciso achar o pq não está achando o dado pedido pelo usuario no dicionario.
Falta modificar as funções de Sessões e criar a de Relatorios


"""