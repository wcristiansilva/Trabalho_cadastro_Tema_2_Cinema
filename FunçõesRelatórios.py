"""
Funções do menu Relatórios

"""


def DadosSalasCapacidade(BDSALAS):
    
    if len(BDSALAS) == 0:
        print("\n AINDA NÃO FORAM FORNECIDOS DADOS! ")
        input("\n TECLE <ENTER>")
    else:
        Capacidade_minima = int(input("\n Digite a Capacidade minima desejada: "))
        Capacidade_maxima = int(input("\n Digite a Capacidade maxima desejada: "))
        
        for sala in BDSALAS:
            lista = BDSALAS[sala]
            lista = list(lista)
            if lista[1] >= Capacidade_minima and lista[1] <= Capacidade_maxima:
                print(f"\n As Salas com a capacidade pedida são: {lista}")
                
                print("\n *** Listagem Pronta ***")
                input("\n TECLE <ENTER> ")
            else:
                print("\n *** Capacidade não encontrada ***")
                input("\n TECLE <ENTER> ")


def DadosFilmesGenero(BDFILMES):
    
    if len(BDFILMES) == 0:
        print("\n AINDA NÃO FORAM FORNECIDOS DADOS! ")
        input("\n TECLE <ENTER>")
    else:
        Genero = input("\n Digite o Gênero desejado: ")

        print(f"\n Os Filmes com o Gênero pedido são: ")        
        for filmes in BDFILMES:
            lista = BDFILMES[filmes]
            #lista = list(lista)
            print(lista)
            if Genero == lista[2]:
                print(f"\n {lista}")
                
                print("\n *** Listagem Pronta ***")
                input("\n TECLE <ENTER> ")
            else:
                print(f"\n *** O Gênero {Genero}, solicitado não Existe! ***")
                input("\n TECLE <ENTER> ")


def DadosSalasFilmesPorData(BDSESSAO, BDSALAS, BDFILMES):

    if len(BDSESSAO) == 0 and len(BDSALAS) == 0 and len(BDFILMES) == 0:
        print("\n AINDA NÃO FORAM FORNECIDOS DADOS! ")
        input("\n TECLE <ENTER>")
    else:
        Data_inicial = input("\nDigite o Ano minimo para pesquisa: ")
        Data_final = input("\nDigite o Ano maximo para pesquisa: ")
        Sessao = BDSESSAO
        Sessao = list(Sessao)
        

        for sessao in Sessao:
            lista_sessao = Sessao[sessao]
            lista = list(lista_sessao)
            if lista[2] >= Data_inicial and lista[2] <= Data_final:
                print(f"\n As Salas com a capacidade pedida são: {lista_sessao}")
