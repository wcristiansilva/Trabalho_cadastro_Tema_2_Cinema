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
        # print(chave,'\n')
        #print(BDSESSAO[key])
        # listakey = []
        # for d in listak:
            # listakey.append(d)
        # print('\nlista key1', listakey, '\n')
        
        # Pegando a lista de chaves e dados:
        #
        # 				   0 				1 
        # BD[(Codigo_do_Filme, Codigo_da_Sala, Data_Sessao, Horário_da_Sessão)] = preco
        # criando uma lista pra receber os dados da tupla que foi salva dentro de outra lista com laço for
        listak = chave[0]
        listakey = []
        for d in listak:
            listakey.append(d)
        # Convertendo a lista que tem as chaves numa string,
        # usando como separador o #:
        stringkey = "#".join([str(i) for i in listakey])
        # Montando a linha que vai ser gravada:
        linha = stringkey + ";" + BDSESSAO[key] + "\n"
        # Gravando a linha no arquivo:
        arq.write(linha)
        #fim do for
    # Fechando o arquivo:
    arq.close()