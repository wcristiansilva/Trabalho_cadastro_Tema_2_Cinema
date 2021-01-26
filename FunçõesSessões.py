"""
Funções do menu Sessões

"""
from datetime import datetime
from FunçõesArquivos import *

# Função para listar todas as Sessões do Dicionário: Falta modificar a função
def ListarTodasSessoes(BDSESSOES):
    
    if len(BDSESSOES) == 0:
        print("\n AINDA NÃO FORAM CADASTRADO DADOS! ")
        input("\n TECLE <ENTER>")
    else:
        for sessao, dados in BDSESSOES.items():
            print(f"\n Sessão: {sessao}  Valor do Ingresso: {dados}")
            # print(f"\n {BDSESSOES} \n")
        print("\n *** Listagem Pronta ***")
        input("\n TECLE <ENTER> ")


# Função para listar uma Sessao do Dicionário fornecido pelo Usuário usando dado inserido pelo mesmo: Pronto essa parte
def ListarUmaSessaoDici(BDSESSOES):

    Procura_lista = input("\n Digite o Código da Sessão para pesquisar: ")

    if Procura_lista in BDSESSOES:
        
        print(f"\n A Procura retornou {BDSESSOES[Procura_lista]}")
    else:
        print("\n ** Não encontrei o que procura ** ")
        input("\n TECLE <ENTER> ")
    print("\n ** Procura Finalizada ** ")
    input("\n TECLE <ENTER> ")


# Função de Inclusão de Sessoes: Pronta essa parte
def IncluirSessao(BDSESSOES, BDSALAS, BDFILMES):

    # Verifica se tem sala e filme cadastrado pra continuar com o cadastro de sessão
    if (len(BDFILMES) == 0 or len(BDSALAS) == 0):
        print("\n** NÃO É POSSIVEL INCLUIR UMA SESSÃO SEM FILMES OU SALAS CADASTRADAS **")
    else:
        # pegando os Códigos que vão ser inserido no dicionário da Sessão:
        print("\n *** Incluindo nova Sessão *** ")
        
        Codigo_do_Filme = int(input("\nDigite o Código do Filme: "))

        # Testa se já tem o código do Filme no dicionário Filmes:
        if Codigo_do_Filme in BDFILMES:
            Codigo_da_Sala = int(input("\nDigite o Códiogo da Sala: "))
            
            # Testa se já tem o código da Sala no dicionário Salas:
            if Codigo_da_Sala in BDSALAS:
                # sala e filme existem!!!!
                # pegando o resto dos dados da sessao:
                
                # inclusão dos dados na lista:
                
                Data_Sessao = input("\nDigite a Data da Sessão: ex:01-01-1001: ")
                
                Horário_da_Sessão = input("\nDigite o Horário da Sessão: ")

                # montando a tupla que vai ser a chave do dicionario sessoes
                
                Codigo_Se = (Codigo_do_Filme, Codigo_da_Sala, Data_Sessao, Horário_da_Sessão)
                # verificando se já existe uma sessão com esses dados
                
                if Codigo_Se not in BDSESSOES:
                    # recebendo o preco do ingresso
                    preco = input("\nDigite o Valor do Ingresso: ")
                    # inclui esta sessao no dicionario:
                    BDSESSOES[Codigo_Se] = preco
                    # print(BDSESSOES)
                    print("\n ** Dados inseridos com sucesso! ** ")

                    ArquivoSessões(BDSESSOES)
                    
                    input("\n TECLE <ENTER> ")
                        
                else:
                    print("\n Uma sessão com esses dados ja existe! ")
                    input("\n TECLE <ENTER> ")
            else:
                print("\n ** Código não Cadastrado ** ")
                input("\n TECLE <ENTER> ")
        else:
            print("\n ** Código não Cadastrado ** ")
            input("\n TECLE <ENTER> ")                  
    
          
# Função para Alterar Dados de uma Sessao ou Excluir uma Sessao inteira ou um Dado passado pelo usuário: Falta modificar a função
def AlterarOuExcluirSessoes(armazenamento):
        # print(armazenamento) # Usado pra visualizar o dic antes de falzer algo durante os teste
    
    Dado = int(input(" Digite o Código do Filme que deseja alterar ou excluir: "))
    if Dado in armazenamento:
        print("\n Para Alterar Digite A ou E para Excluir: ")
        op = str(input("\n Deseja apagar ou excluir? ")).upper()[0]

        # print(op) # Usado pra ver se a variavel estava recebendo o valor correto durante os teste

        # Recebe a lista do dicionario e faz alteração por indice.
        if op == 'A':
            altera_Preco = armazenamento[Dado]
            print("\nDados da Sessão pesquisada abaixo: ")
            print(altera_Preco)
            altera_Dado = input("\nDigite o novo Preço do Ingresso: ")
            if altera_Dado in altera_Preco:
                i = altera_Preco.index(altera_Dado)
                novo_dado = input("\nDigite o novo Preço a ser salvo: ")
                altera_Preco.pop(i)
                altera_Preco.insert(i, novo_dado)
                nova_lista = altera_Preco
                armazenamento[Dado] = nova_lista
                print("\n ** DADO ALTERADO COM SUCESSO **")
                input("\n TECLE <ENTER> ")
            else:
                print(f"\nO {altera_Dado} não consta nos arquivos salvos. \n")
                input("\n TECLE <ENTER> ")

        # Recebe a lista do dicionário e faz a exclusão da Sessão.
        elif op == 'E':
            print("\nDeseja realmente deletar a Sessão? ")
            escolha_deleta = input("\nDigite S para deletar a Sessão ou N para desistir: ").upper()[0]

            if escolha_deleta == 'S':
                del armazenamento[Dado]
                print("\n Excluido com Sucesso! ")
                input("\n TECLE <ENTER>  ")
            elif escolha_deleta == 'N':
                print("\n Sessão não foi excluida! ")
            else:
                print("\n ERRO!!! Opção Inválida!! ")
                input("\n TECLE <ENTER> ")
        else:
            print("\n ERRO!!! Opção Inválida!! ")
            input("\n TECLE <ENTER> ")
    else:
        print("\n NÃO FOI ENCONTRADO O DADO ESPECIFICADO! ")
        input("\n TECLE <ENTER> ")
