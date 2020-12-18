"""
Funções do menu Filmes
"""


# Função para listar todos os Filmes do Dicionário:
def ListarTodosFilmes(armazenamento):
    
    if len(armazenamento) == 0:
        print("\n AINDA NÃO FORAM FORNECIDOS DADOS! ")
        input("\n TECLE <ENTER>")
    else:
        for k, v in armazenamento.items():
            print(f"\n Código {k} pertence ao Filme: {v}")
        print("\n *** Listagem Pronta ***")
        input("\n TECLE <ENTER> ")


# Função para listar um Filme do Dicionário fornecido pelo Usuário pelo Código.
def ListaUmFilmeDici(armazenamento):

    Procura_lista = input("\n Digite o Código do Filme que deseja pesquisar: ")

    if Procura_lista in armazenamento:
        
        print(f"\n A Procura retornou {armazenamento[Procura_lista]}")
    else:
        print("\n Não encontrei o que procura ")
        input("\n TECLE <ENTER> ")
    print("\n ** Procura Finalizada ** ")
    input("\n TECLE <ENTER> ")


# Função de Inclusão de Filmes:
def IncluirFilmes(armazenamento):      
   
    # pegando o Código que vai ser inserindo no dicionário do Filme:
    print("\n *** Incluindo novo Filme *** ")
    Codigo_F = int(input("\nDigite o Código do Filme:"))

    # Testa se já tem o código no dicionário:
    if Codigo_F in armazenamento:
        print("\n ** Código Existente no Sistema ** ")
        input("\n TECLE <ENTER> ")

    else:
        # cria uma lista vazia:
        Dados_Filmes = []
        # inclusão dos dados na lista:
        Nome = input("Digite o nome do Filme:")
        AnoLancamento = input("Digite o Ano de Lançamento:")
        Genero = input("Digite o Gênero:")

        # Adiciona os Dados na Lista Dados_Filmes:
        Dados_Filmes.append(Nome)
        Dados_Filmes.append(AnoLancamento)
        Dados_Filmes.append(Genero)

        # Recebe a quantidade de atores que tem no Filme Cadastrado:
        QtAtores = int(input("\n Quantos Atores tem o Filme: "))

        # Cria uma lista para os atores e um contador pro laço enquanto.
        Lst_Atores = []
        cont = 0

        # Laço Enquanto para adicionar a quantidade de atores passada pelo usuário:
        while cont < QtAtores:
            Atores = input("\nDigite os Atores: ")
            Lst_Atores.append(Atores)
            cont += 1
        Dados_Filmes.append(Lst_Atores)

        # inclui no dicionario o código e a lista com os dados do código cadastrado:
        armazenamento[Codigo_F] = Dados_Filmes

        print("\n ** Dados inseridos com sucesso!** ")

        input("\n TECLE <ENTER> ")   


# Função para Alterar Dados de um Filme ou Excluir um Filme inteira ou um Dado passado pelo usuário.
def AlterarOuExcluirFilmes(armazenamento):
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

