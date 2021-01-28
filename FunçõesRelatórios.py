"""
Funções do menu Relatórios

"""
from datetime import *

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
            lista_Int = int(lista[1])
            if lista_Int >= Capacidade_minima and lista_Int <= Capacidade_maxima:
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
        Genero = input("\n Digite o Gênero desejado: ").upper()

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


def compara1(c1, d2):  # Função para comparar e retorna um valor se for o pedido para a função DadosSalasFilmesPorData
    c1 = datetime.strptime(c1, "%d/%m/%Y")
    d2 = datetime.strptime(d2, "%d/%m/%Y")

    if c1 >= d2:
        return 1
    else:
        return 0


def compara2(d1, d2):  # Função para comparar e retorna um valor se for o pedido para a função DadosSalasFilmesPorData
    c1 = datetime.strptime(d1, "%d/%m/%Y")
    d2 = datetime.strptime(d2, "%d/%m/%Y")

    if c1 <= d2:
        return -1
    else:
        return 0


def DadosSalasFilmesPorData(BDSESSAO, BDSALAS, BDFILMES):  # Função para mostrar sa sessao a sala e o filme de um intervalo de data pasado pelo usuario.
    if len(BDSESSAO) == 0 or len(BDSALAS) == 0 or len(BDFILMES) == 0:
        print("\n AINDA NÃO FORAM FORNECIDOS DADOS! ")
        input("\n TECLE <ENTER>")
    else:
        Str_Data_inicial = input("\nDigite a data minima para pesquisa: Ex: 14/02/2020. ")

        Str_Data_final = input("\nDigite a data maxima para pesquisa: Ex: 14/02/2020. ")
        
        for k, v in BDSESSAO.items():
            if compara1(k[2], Str_Data_inicial) == 1 and compara2(k[2], Str_Data_final) == -1:
                if k[1] in BDSALAS and k[0] in BDFILMES:           
                    print(f"\n A Procura retornou a Sessão {k} preço do ingresso R${v}, que vai ser na Sala {BDSALAS[k[1]]}, e será passado o seguinte Filme {BDFILMES[k[0]]}.")

        print("\n ** Procura Finalizada ** ")
        input("\n TECLE <ENTER> ")