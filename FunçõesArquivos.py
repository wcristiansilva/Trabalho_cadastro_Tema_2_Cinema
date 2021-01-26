"""
Funções para Criar o Arquivo do Dicionario

"""


def ArquivoSala(BDSALAS):
    arq = open("BDSALAS.txt", "a")
    # Vamos percorrer o dicionário inteiro:
    for Codigo_Sa in BDSALAS:
        # Pegando a lista de dados:
        #
        # 0 1 
        # BDSALAS[Codigo_Sa] = [ "Nome" , "Capacidade", "Tipo de Exibição", "Acessibilidade" ]
        listadados = BDSALAS[Codigo_Sa][0]
        # Convertendo os dados em uma string,
        # usando como separador o #:
        stringdados = "#".join(listadados)
        # Montando a linha que vai ser gravada:
        linha = Codigo_Sa + ";" + stringdados + "\n"
        # Gravando a linha no arquivo:
        arq.write(linha)
        #fim do for
    # Fechando o arquivo:
    arq.close()


def ArquivoFilme(BDFILMES):
    arq = open("BDFILMES.txt", "a")
    # Vamos percorrer o dicionário inteiro:
    for Codigo_F in BDFILMES:
        # Pegando a lista de dados:
        #
        #      chave                      0                                1 
        # BD[Codigo_F] = [ "Nome", "Ano Lançamento", "Genero", [ ator1, ator2, ator3 ] ]
        listaatores = BDFILMES[Codigo_F][1]
        listadados = BDFILMES[Codigo_F][0]
        # Convertendo a lista de atores em uma string,
        # usando como separador o #:
        stringatores = "#".join(listaatores)
        # Convertendo a lista de dados em uma string,
        # usando como separador o #:
        stringdados = "*".join(listadados)
        # Montando a linha que vai ser gravada:
        linha = Codigo_F + ";" + stringdados + ";" + stringatores + "\n"
        # Gravando a linha no arquivo:
        arq.write(linha)
        #fim do for
    # Fechando o arquivo:
    arq.close()


def ArquivoSessões():
    print("teste")