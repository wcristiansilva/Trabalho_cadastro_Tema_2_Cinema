"""
Funções do menu Filmes

"""
from FunçõesArquivos import *

# Função para listar todos os Filmes do Dicionário:
def ListarTodosFilmes(BDFILMES):
   # Lista_Todas = armazenamento
    if len(BDFILMES) == 0:
        print("\n AINDA NÃO FORAM CADASTRADO DADOS! ")
        input("\n TECLE <ENTER>")
    else:
        for filme, dados in BDFILMES.items():
            print(f"\n Código do Filme: {filme} Dados: {dados}", end='')
            # print(f"\n {BDFILMES} \n")
        print("\n\n *** Listagem Pronta ***")
        input("\n TECLE <ENTER> ")


# Função para listar um Filme do Dicionário fornecido pelo Usuário pelo Código.
def ListaUmFilmeDici(BDFILMES):
    if len(BDFILMES) == 0:
        print("\n AINDA NÃO FORAM CADASTRADO DADOS! ")
        input("\n TECLE <ENTER>")
    else:
        Procura_lista = int(input("\n Digite o Código do Filme que deseja pesquisar: "))

        if Procura_lista in BDFILMES:
            print(f"\n A Procura retornou a Sala com o Código: {Procura_lista} e seus Dados: {BDFILMES[Procura_lista]}")
        else:
            print("\n Não encontrei o que procura ")
            input("\n TECLE <ENTER> ")
    print("\n ** Procura Finalizada ** ")
    input("\n TECLE <ENTER> ")


# Função de Inclusão de Filmes:
def IncluirFilmes(BDFILMES):      
   
    # pegando o Código que vai ser inserindo no dicionário do Filme:
    print("\n *** Incluindo novo Filme *** ")
    Codigo_F = input("\nDigite o Código do Filme: ")

    # Testa se já tem o código no dicionário:
    if Codigo_F in BDFILMES:
        print("\n ** Código Existente no Sistema ** ")
        input("\n TECLE <ENTER> ")

    else:
        # cria uma lista vazia:
        Dados_Filmes = []
        # inclusão dos dados na lista:
        Nome = input("Digite o nome do Filme: ")
        AnoLancamento = input("Digite o Ano de Lançamento: ")
        Genero = input("Digite o Gênero: ").upper()

        # Adiciona os Dados na Lista Dados_Filmes:
        Dados_Filmes.append(Nome)
        Dados_Filmes.append(AnoLancamento)
        Dados_Filmes.append(Genero)

        # Recebe a quantidade de atores que tem no Filme Cadastrado:
        QtAtores = int(input("\nQuantos Atores tem o Filme: "))

        # Cria uma lista para os atores e um contador pro laço enquanto.
        Lst_Atores = []
        cont = 0

        # Laço Enquanto para adicionar a quantidade de atores passada pelo usuário:
        while cont < QtAtores:
            Atores = input("\nDigite os Atores: ")
            Lst_Atores.append(Atores)
            cont += 1
        # inclui os dados dos atores na lista lst atores e depois cria uma tupla com o codigo informado para o filme.
        Dados_Filmes.append(Lst_Atores)
        
        # inclui no dicionario o código e a lista com os dados do código cadastrado:
        BDFILMES[Codigo_F] = Dados_Filmes

        print("\n ** Dados inseridos com sucesso! ** ")

        ArquivoFilme(BDFILMES)

        input("\n TECLE <ENTER> ")


# Função para Alterar Dados de um Filme ou Excluir um Filme inteira ou um Dado passado pelo usuário.
def AlterarOuExcluirFilmes(BDFILMES): 
        # print(armazenamento) # Usado pra visualizar o dic antes de falzer algo durante os teste
    
    Dado = input(" Digite o Código do Filme que deseja alterar ou excluir: ")
    if Dado in BDFILMES:
        print("\n Para Alterar Digite A ou E para Excluir: ")
        op = input("\n Deseja apagar ou excluir? ").upper()[0]

        # print(op) # Usado pra ver se a variavel estava recebendo o valor correto durante os teste

        # Recebe a lista do dicionario e faz alteração por indice.
        if op == 'A':
            print("\n** ALTERANDO DADOS **")
            altera_lista = BDFILMES[Dado]
            altera_sublista = BDFILMES[Dado][3]
            print("\nDados do Filme pesquisado abaixo: ")
            print(altera_lista)
            altera_Dado = input("\nO que deseja alterar do Filme com base no mostrado acima: ")
            if altera_Dado in altera_lista:
                i = altera_lista.index(altera_Dado)
                novo_dado = input("\nDigite o novo Dado a ser salvo: ")
                altera_lista.pop(i)
                altera_lista.insert(i, novo_dado)
                nova_lista = altera_lista
                BDFILMES[Dado] = nova_lista
                print("\n ** DADO ALTERADO COM SUCESSO **")
                input("\n TECLE <ENTER> ")

            elif altera_Dado in altera_sublista:
                i = altera_sublista.index(altera_Dado)
                novo_dado = input("\nDigite o novo Dado a ser salvo: ")
                altera_sublista.pop(i)
                altera_sublista.insert(i, novo_dado)
                altera_lista.pop(3)
                altera_lista.insert(3, altera_sublista)
                BDFILMES[Dado] = altera_lista
                print("\n ** DADO ALTERADO COM SUCESSO **")
                input("\n TECLE <ENTER> ")
            else:
                print(f"\nO dado {altera_Dado} não consta nos arquivos salvos. \n")
                input("\n TECLE <ENTER> ")
                

        # Recebe a lista do dicionário e faz a exclusão do Filme todo ou só um dado expecifico por índice.
        elif op == 'E':
            print("\nDeseja deletar todos os dados do Filme ou somente um?")
            escolha_deleta = input("\nDigite T para deletar o Filme todo ou D para somente um Dado especifico: ").upper()[0]

            if escolha_deleta == 'D':
                deleta_lista = BDFILMES[Dado]
                deleta_sublista = BDFILMES[Dado][3]
                print("\nDados do Filme pesquisada abaixo: ")
                print(deleta_lista)
                deleta_Dado = input("\nO que deseja deletar do Filme com base no mostrado acima: ")
                # apaga o dado passado pelo usúario na lista
                if deleta_Dado in deleta_lista:
                    i = deleta_lista.index(deleta_Dado)
                    #novo_dado = input("\nDigite o novo Dado a ser Deletado: ")
                    deleta_lista.pop(i)
                    #deleta_lista.insert(i, novo_dado)
                    nova_lista = deleta_lista
                    BDFILMES[Dado] = nova_lista
                    print("\n ** DADO EXCLUIDO COM SUCESSO!! ** ")
                    input("\n TECLE <ENTER> ")
                # apaga o dado passado pelo usúario na sublista
                elif deleta_Dado in deleta_sublista:
                    i = deleta_sublista.index(deleta_Dado)
                    #novo_dado = input("\nDigite o novo Dado a ser salvo: ")
                    deleta_sublista.pop(i)
                    #deleta_sublista.insert(i, novo_dado)
                    deleta_lista.pop(3)
                    deleta_lista.insert(3, deleta_sublista)
                    BDFILMES[Dado] = deleta_lista
                    print("\n ** DADO EXCLUIDO COM SUCESSO **")
                    input("\n TECLE <ENTER> ")
                else:
                    print(f"\nO {deleta_Dado} não consta nos arquivos salvos. ")
                    input("\n TECLE <ENTER> ")
            elif escolha_deleta == 'T':
                del BDFILMES[Dado]
                print("\n Excluido com Sucesso! ")
                input("\n TECLE <ENTER>  ")
            
            else:
                print("\n ERRO!!! Opção Inválida!! ")
                input("\n TECLE <ENTER> ")
        else:
            print("\n ERRO!!! Opção Inválida!! ")
            input("\n TECLE <ENTER> ")
    else:
        print("\n NÃO FOI ENCONTRADO O DADO ESPECIFICADO! ")
        input("\n TECLE <ENTER> ")
