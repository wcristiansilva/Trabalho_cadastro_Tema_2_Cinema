from FunçõesFilme import *
from FunçõesSala import *
from FunçõesSessões import *
from FunçõesRelatórios import *
from FunçõesArquivos import *


def Menu():
    # Declaração de Dicionários

    BDSALAS = {}
    BDFILMES = {}
    BDSESSAO = {}
    
    # Passando os dados dos arquivos para os dicionarios

    InsereSalasArq(BDSALAS)
    InsereFilmesArq(BDFILMES)
    InserSessoesArq(BDSESSAO)

    # Variaveis para ser usadas nos laço while do menu e submenu.
    opcao = 0
    subopcao = 0
    while opcao != 5:  # Menu Inicial
        subopcao = 0
        print("\n1 - Submenu de Salas")
        print("2 - Submenu de Filmes")
        print("3 - Submenu de Sessões")
        print("4 - Submenu Relatórios")
        print("5 - Sair")
        opcao = int(input("\nDigite a opcao desejada: "))
        while opcao < 1 or opcao > 5:
            print("\n Opcao invalida!")
            opcao = 0
            opcao = int(input("\nDigite a opcao desejada: "))

        if opcao == 1:  # Submenu Salas
            while subopcao != 5:
                print("\n1 - Listar Salas")
                print("2 - Listar uma Sala do Cadastro")
                print("3 - Incluir Sala")
                print("4 - Alterar ou Excluir informação da Sala")
                print("5 - Voltar para o Menu Inicial")

                subopcao = int(input("\n Digite a opcao desejada: "))
                while subopcao < 1 or subopcao > 5:
                    print("\n Opcao invalida!")
                    subopcao = int(input("\n Digite a opcao desejada: "))

                if subopcao == 1:
                    ListaTodasSalas(BDSALAS)
                if subopcao == 2:
                    ListaUmaSalaDici(BDSALAS)
                if subopcao == 3:
                    IncluirSala(BDSALAS)
                if subopcao == 4:
                    AlterarOuExcluirSalas(BDSALAS)
                if subopcao == 5:
                    print("\nVoltando ao Menu Principal!")
        elif opcao == 2:  # Submenu Filmes
            while subopcao != 5:
                print("\n1 - Listar Filmes:")
                print("2 - Listar um Elemento do Filme:")
                print("3 - Incluir Filme:")
                print("4 - Alterar ou Excluir informação da Filme:")
                print("5 - Voltar para o Menu Inicial:")

                subopcao = int(input("\nDigite a opcao desejada: "))
                while subopcao < 1 or subopcao > 5:
                    print("\nOpcao invalida!")
                    subopcao = int(input("\nDigite a opcao desejada: "))

                if subopcao == 1:
                    ListarTodosFilmes(BDFILMES)
                elif subopcao == 2:
                    ListaUmFilmeDici(BDFILMES)
                elif subopcao == 3:
                    IncluirFilmes(BDFILMES)
                elif subopcao == 4:
                    AlterarOuExcluirFilmes(BDFILMES)
                elif subopcao == 5:
                    print("\nVoltando ao Menu Principal!")
        elif opcao == 3: # Submenu Sessões
            while subopcao != 5:
                print("\n1 - Listar Sessões")
                print("2 - Listar um Elemento de uma Sessão")
                print("3 - Incluir Sessao")
                print("4 - Alterar ou Excluir informação de uma Sessões")
                print("5 - Voltar ao menu Principal")

                subopcao = int(input("\nDigite a opcao desejada: "))

                while subopcao < 1 or subopcao > 5:
                    print("\nOpcao invalida!")
                    subopcao = int(input("\nDigite a opcao desejada: "))

                if subopcao == 1:
                    ListarTodasSessoes(BDSESSAO)
                elif subopcao == 2:
                    ListarUmaSessaoDici(BDSESSAO)
                elif subopcao == 3:
                    IncluirSessao(BDSESSAO, BDSALAS, BDFILMES)
                elif subopcao == 4:
                    AlterarOuExcluirSessoes(BDSESSAO)
                elif subopcao == 5:
                    print("\nVoltando ao Menu Principal!")
        elif opcao == 4:  #Submenu Relatórios
            while subopcao != 4:
                print("\n1 - Listar Salas entre a Capacidade desejada:")
                print("2 - Listar um Filme do Gênero desejado:")
                print("3 - Listar Filme, Sala e Sessão por um intervalo de datas:")
                print("4 - Voltar para o Menu Inicial: \n")

                subopcao = int(input("\nDigite a opcao desejada: "))
                while subopcao < 1 or subopcao > 4:
                    print("\n ** Opção invalida! ** ")
                    opcao = 0
                    subopcao = int(input("\nDigite a opcao desejada: "))
                if subopcao == 1:
                    DadosSalasCapacidade(BDSALAS)
                elif subopcao == 2:
                    DadosFilmesGenero(BDFILMES)
                elif subopcao == 3:
                    DadosSalasFilmesPorData(BDSESSAO, BDSALAS, BDFILMES)
                elif subopcao == 4:
                    print("\n ** Voltando ao Menu Principal! ** ")
        elif opcao == 5:  #Submenu Finalizar Programa
            print("\n** programa finalizado **\n\n")
            break


"""

Partiu arquivos dos dicionarios e pau pra quem te quer, que Deus me ajude kkk
falta fazer o arquivo de sessoes e depois criar aqui no menu a funcao para jogar tudo dentro do dicionario novamente.

"""