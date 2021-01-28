"""

Funções para Criar o Arquivo do Dicionario

"""


def ArquivoSala(BDSALAS):
    arq = open("BDSALAS.txt", "w")
    # Vamos percorrer o dicionário inteiro:
    for Codigo_Sa in BDSALAS:
        # Pegando a lista de dados:
        #
        #             Key           0           1               2                   3 
        # BDSALAS[Codigo_Sa] = [ "Codigo_F" , "Capacidade", "Tipo de Exibição", "Acessibilidade" ]
        listadados = BDSALAS[Codigo_Sa]
        # Convertendo os dados em uma string,
        # usando como separador o #:
        stringdados = "#".join(listadados)
        # Montando a linha que vai ser gravada:
        Codigo_Sa_Str = "".join(str(Codigo_Sa))
        linha = Codigo_Sa_Str + ";" + stringdados + "\n"
        # Gravando a linha no arquivo:
        arq.write(linha)
        #fim do for
    # Fechando o arquivo:
    arq.close()


def ArquivoFilme(BDFILMES):
    arq = open("BDFILMES.txt", "w")
    # Vamos percorrer o dicionário inteiro:
    for Codigo_F in BDFILMES:
        # Pegando a lista de dados:
        #
        #      Key                   0               1             2                3
        # BDFILMES[Codigo_F] = [ "Codigo_F", "Ano Lançamento", "Genero", [ ator1, ator2, ator3 ] ]
        listaatores = BDFILMES[Codigo_F][3]
        # Convertendo a lista de atores em uma string,
        # usando como separador o #:
        stringatores = "#".join(listaatores)
        # Montando a linha que vai ser gravada:
        Codigo_F_Str = "".join(str(Codigo_F))
        linha = Codigo_F_Str + ";" + BDFILMES[Codigo_F][0] + ";" + BDFILMES[Codigo_F][1] + ";" + BDFILMES[Codigo_F][2] + ";" + stringatores + "\n"
        # Gravando a linha no arquivo:
        arq.write(linha)
        #fim do for
    # Fechando o arquivo:
    arq.close()


def ArquivoSessões(BDSESSAO):
    arq = open("BDSESSAO.txt", "w")
    # Vamos percorrer o dicionário inteiro:
    chave = []
    for key in BDSESSAO:
        del chave [:]
        chave.append(key)        
        # Pegando a lista de chaves e dados:
        #
        # 				   0 				1 
        # BDSESSAO[(Codigo_do_Filme, Codigo_da_Sala, Data_Sessao, Horário_da_Sessão)] : preco
        # criando uma lista pra receber os dados da tupla que foi salva dentro de outra lista com laço for
        listak = chave[0]
        listakey = []
        for d in listak:
            listakey.append(d)
        
        lista = BDSESSAO[key][0]
        # Convertendo a lista que tem as chaves numa string,
        # usando como separador o #:
        stringkey = "#".join(str(lista) )
        # Montando a linha que vai ser gravada:
        linha = stringkey + "#" + BDSESSAO[key] + "\n"
        # Gravando a linha no arquivo:
        arq.write(linha)
        #fim do for
    # Fechando o arquivo:
    arq.close()



"""

Funções para inserir dados do Arquivo no Dicionario

"""


def InsereSalasArq(BDSALAS):
    # Abrindo arquivo para leitura:
    arq = open("BDSALAS.txt", "r")
    # Percorrendo as linhas do arquivo:
    for linha in arq:
        
        # removendo o \n do final da linha:
        linha = linha[:len(linha)-1] 
        
        # a linha é:
        # 1;sala1#3#0#0 [1,sala1#3#0#0]
        #
        # Vamos quebrar por ;
        lista = linha.split(";")
        # codigo está em lista[0]
        # nome da sala está em lista[1]
        # capacidade em lista[2]
        # Tipo de Exibição em lista[3]
        # Acessibilidade em lista[4]
        # vamos gerar uma nova lista,
        # agora com os telefones,
        # usando o split com #
        listadados = lista[1].split("#") # [1,sala1,3,0,0]
        # Colocando os dados no dicionario:
        BDSALAS[ lista[0] ] =  listadados
        ##fim for
    # Exibindo o dicionário:
    arq.close()


def InsereFilmesArq(BDFILMES):
    # Abrindo arquivo para leitura:
    arq = open("BDFILMES.txt", "r")

    # Percorrendo as linhas do arquivo:
    for linha in arq:

        # a linha é:
        # 1;as;as;as;a1#a1
        #
        # Vamos quebrar por ;
        linha = linha[:len(linha)-1]
        lista = linha.split(";")


        # codigo está em lista[0]
        # nome está em lista[1]
        # ano de lançamento em lista[2}
        # genero em lista[3]
        # todos os atores estão em lista[4]

        # vamos gerar uma nova lista,
        # agora com os atores,
        # usando o split com #
        # BDFILMES[Codigo_F] = [ "nome", "Ano Lançamento", "Genero", [ ator1, ator2, ator3 ] ]
        # [key, nome, Ano Lançamento, genero, [ ator1, ator2, ator3 ]]
        listaatores = lista[4].split("#")

        # Colocando os dados no dicionario:

        BDFILMES[ lista[0] ] =  [lista[1], lista[2], lista[3], listaatores]

    ##fim for
    arq.close()


def InserSessoesArq(BDSESSAO):
    # Abrindo arquivo para leitura:
    arq = open("BDSESSAO.txt", "r")

    # Percorrendo as linhas do arquivo:
    for linha in arq:

        # removendo o \n do final da linha:
        linha = linha[:len(linha)-1]
        # a linha é:
        # 1#1#14/03/2020#15:00;25,00
        #
        # Vamos quebrar por ;
        lista = linha.split("#") # [1# 1# 14/03/2020# 15:00# 25,00]
        # codigo filme está em lista[0]
        # codigo sala está em lista[1]
        # data de exibição em lista[2]
        # hr da Exibição em lista[3]
        # preco em lista[4]
        # vamos gerar uma nova lista
        # agora com o preço
        # usando o split com ;
        # BDSESSAO[(Codigo_do_Filme, Codigo_da_Sala, Data_Sessao, Horário_da_Sessão)] : preco
        # [(Codigo_do_Filme, Codigo_da_Sala, Data_Sessao, Horário_da_Sessão)] : preco
        preco = lista[4] # .split("#")

        # Colocando os dados no dicionario:

        BDSESSAO[ lista[0], lista[1], lista[2], lista[3] ] = preco

    ##fim for
    arq.close()