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
            print(f"\n Código {k} pertence ao Filme: {v}")
        print("\n *** Listagem Pronta ***")
        input("\n TECLE <ENTER> ")


# Função para listar uma Sessao do Dicionário fornecido pelo Usuário usando o Código do mesmo: Falta modificar a função
def ListaUmaSessaoDici(armazenamento):

    Procura_lista = input("\n Digite o Código do Filme que deseja pesquisar: ")

    if Procura_lista in armazenamento:
        
        print(f"\n A Procura retornou {armazenamento[Procura_lista]}")
    else:
        print("\n Não encontrei o que procura ")
        input("\n TECLE <ENTER> ")
    print("\n ** Procura Finalizada ** ")
    input("\n TECLE <ENTER> ")


# Função de Inclusão de Sessoes: Pronta essa parte
def IncluirSessao(armazenamento, BDSALA, BDFILMES):      

    # pegando o Código que vai ser inserindo no dicionário da Sessão:

    print("\n *** Incluindo nova Sessão *** ")
    
    Codigo_Filmes = input("\n Digite o Código do Filme: ")
    
    # Testa se já tem o código do Filme no dicionário:
    if Codigo_Filmes not in BDFILMES: 
        Codigo_SALAS = input("\n Digite o Códiogo da Sala: ")
        # Testa se já tem o código da Sala no dicionário:
        if Codigo_SALAS not in BDSALA:              
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
            altera_lista = armazenamento[Dado]
            print("\nDados do Filme pesquisado abaixo: ")
            print(altera_lista)
            altera_Dado = input("\nO que deseja alterar do Filme com base no mostrado acima: ")
            if altera_Dado in altera_lista:
                i = altera_lista.index(altera_Dado)
                novo_dado = input("\nDigite o novo Dado a ser salvo: ")
                altera_lista.pop(i)
                altera_lista.insert(i, novo_dado)
                nova_lista = altera_lista
                armazenamento[Dado] = nova_lista
                input("\n TECLE <ENTER> ")
            else:
                print(f"\nO {altera_Dado} não consta nos arquivos salvos. \n")
                input("\n TECLE <ENTER> ")

        # Recebe a lista do dicionário e faz a exclusão do Filme todo ou só um dado expecifico por índice.
        elif op == 'E':
            print("\nDeseja deletar todos os dados do Filme ou somente um?")
            escolha_deleta = print("\nDigite L para deletar o Filme todo ou D para somente um Dado especifico: ")
            escolha_deleta = escolha_deleta.upper()

            if escolha_deleta == 'D':
                deleta_lista = armazenamento[Dado]
                print("\nDados do Filme pesquisada abaixo: ")
                print(deleta_lista)
                deleta_Dado = input("\nO que deseja alterar do Filme com base no mostrado acima: ")
                if deleta_Dado in deleta_lista:
                    i = deleta_lista.index(deleta_Dado)
                    novo_dado = input("\nDigite o novo Dado a ser salvo: ")
                    deleta_lista.pop(i)
                    print("\n **EXCLUIDO DADO COM SUCESSO!!** ")
                    deleta_lista.insert(i, novo_dado)
                    nova_lista = deleta_lista
                    armazenamento[Dado] = nova_lista
                    input("\n TECLE <ENTER> ")
                else:
                    print(f"\nO {deleta_Dado} não consta nos arquivos salvos. ")
                    input("\n TECLE <ENTER> ")
            elif escolha_deleta == 'L':
                del armazenamento[Dado]
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

