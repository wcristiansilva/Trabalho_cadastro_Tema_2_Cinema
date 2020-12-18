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
    


def AlterarOuExcluirFilmes():
    print("Teste")
