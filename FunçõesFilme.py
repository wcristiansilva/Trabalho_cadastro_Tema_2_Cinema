"""
Funções do menu Filmes
"""


def ListarTodosFilmes():
    print("Teste")


def ListarElementoFilme():
    print("Teste")


def IncluirFilmes():  # falta tratar  a entrada de código existente no BD.
    Filmes = []
    CodigoFilme = []
    LstAtores = []

    cont = 0
    # cont1 = True

    # pegando dados e inserindo na lista de filmes:
    # while cont1 != False:
    Codigo = int(input("Digite o Código do Filmes:"))
    # if Codigo in CodigoFilme:
    # print("** Código Existente no Sistema **")

    # else:
    Nome = input("Digite o nome do Filme:")
    AnoLancamento = input("Digite o Ano de Lançamento:")
    Genero = input("Digite o Gênero:")

    CodigoFilme.append(Codigo)
    CodigoFilme.append(Nome)
    CodigoFilme.append(AnoLancamento)
    CodigoFilme.append(Genero)

    QtAtores = int(input("Quantos Atores tem o Filme: "))

    while cont < QtAtores:
        Atores = input("Digite os Atores: ")
        LstAtores.append(Atores)
        cont += 1
    CodigoFilme.append(LstAtores)

    """
    testei inclusão de filme sem sair da função

    QTFilme = input("Se Deseja Adicionar mais Filmes Digite 'sim':")


    if QTFilme == 'sim' or QTFilme == 'SIM':
        cont = 0
        cont1 = True
    else:
        cont1 = False
    """
    Filmes.append(CodigoFilme)
    # print(Filmes)

    print("** Dados inseridos com sucesso!**")

    input("Tecle <enter>")
    return Filmes


def AlterarOuExcluirFilmes():
    print("Teste")
