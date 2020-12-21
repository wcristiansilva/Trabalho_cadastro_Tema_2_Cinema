"""
Funções do menu Sessões
"""


# Função para listar todas as Sessões do Dicionário: Falta modificar a função
def ListarTodasSessoes(armazenamento):
    
    if len(armazenamento) == 0:
        print("\n AINDA NÃO FORAM FORNECIDOS DADOS! ")
        input("\n TECLE <ENTER>")
    else:
        for k, v in armazenamento.items():
            print(f"\n Dados da Sessão {k} Horário da Sessão: {v}")
        print("\n *** Listagem Pronta ***")
        input("\n TECLE <ENTER> ")


# Função para listar uma Sessao do Dicionário fornecido pelo Usuário usando dado inserido pelo mesmo: Falta modificar a função
def ListarUmaSessaoDici(armazenamento):

    Procura_lista = input("\n Digite o Código do Filme para procurar a Sessão: ")

    if Procura_lista in armazenamento:
        
        print(f"\n A Procura retornou {armazenamento[Procura_lista]}")
    else:
        print("\n Não encontrei o que procura ")
        input("\n TECLE <ENTER> ")
    print("\n ** Procura Finalizada ** ")
    input("\n TECLE <ENTER> ")


# Função de Inclusão de Sessoes: Pronta essa parte
def IncluirSessao(armazenamento, BDSALAS, BDFILMES):      

    # pegando o Código que vai ser inserindo no dicionário da Sessão:
    print(BDFILMES)
    print(BDSALAS)

    print("\n *** Incluindo nova Sessão *** ")
    
    Codigo_Filmes = input("\n Digite o Código do Filme: ")
    
    # Testa se já tem o código do Filme no dicionário:
    if Codigo_Filmes in BDFILMES: 
        Codigo_SALAS = input("\n Digite o Códiogo da Sala: ")
        # Testa se já tem o código da Sala no dicionário:
        if Codigo_SALAS in BDSALAS:              
            # cria uma lista vazia:
            Dados_NMuda_Sessao = []
            Dados_Sessao = []
            # inclusão dos dados na lista:
            Data = input("\nDigite a Data da Sessão: ")
            if Data not in armazenamento:
                Horario = input("\nDigite o Horário da Sessão: ")
                if Horario not in armazenamento:
                    Preco_Ingresso = input("\nDigite o Valor do Ingresso: ")

                    # Adiciona os Dados na Lista Dados_Sessao e Dados_NMuda_Sessao:
                    Dados_NMuda_Sessao.append(Codigo_Filmes)
                    Dados_NMuda_Sessao.append(Codigo_SALAS)
                    Dados_NMuda_Sessao.append(Data)
                    Dados_NMuda_Sessao.append(Horario)
                    Dados_Sessao.append(Preco_Ingresso)

                    # Tranforma a Lista com os códigos em tupla pra não serem alterados:
                    Codigo_S = tuple(Dados_NMuda_Sessao)

                    # inclui no dicionario o código e a lista com os dados do código cadastrado:
                    armazenamento[Codigo_S] = Dados_Sessao

                    print("\n ** Dados inseridos com sucesso!** ")

                    input("\n TECLE <ENTER> ")
                    
                else:
                    print("\n Horário não está Disponível! ")
                    input("\n TECLE <ENTER> ")
            else:
                print("\n Data não está Disponível! ")
                input("\n TECLE <ENTER> ")
        else:
            print("\n Código da Sala não Existe! ")
            input("\n TECLE <ENTER> ")
    else:
        print("\n Código do Filme não Existe! ")
        input("\n TECLE <ENTER> ")
                     
          
# Função para Alterar Dados de uma Sessao ou Excluir uma Sessao inteira ou um Dado passado pelo usuário: Falta modificar a função
def AlterarOuExcluirSessoes(armazenamento):
        # print(armazenamento) # Usado pra visualizar o dic antes de falzer algo durante os teste
    
    Dado = input(" Digite o Código do Filme que deseja alterar ou excluir: ")
    if Dado in armazenamento:
        print("\n Para Alterar Digite A ou E para Excluir: ")
        op = str(input("\n Deseja apagar ou excluir? "))
        op = op.upper()

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
                input("\n TECLE <ENTER> ")
            else:
                print(f"\nO {altera_Dado} não consta nos arquivos salvos. \n")
                input("\n TECLE <ENTER> ")

        # Recebe a lista do dicionário e faz a exclusão da Sessão.
        elif op == 'E':
            print("\nDeseja realmente deletar a Sessão? ")
            escolha_deleta = print("\nDigite S para deletar a Sessão ou N para desistir: ")
            escolha_deleta = escolha_deleta.upper()

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

