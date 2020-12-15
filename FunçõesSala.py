"""
Funções do menu Salas
"""


# Função para listar todas as Salas no Dicionário:
def ListaTodasSalas(armazenamento):
    Lista_Todas = armazenamento
    if len(Lista_Todas) == 0:
        print("AINDA NÃO FORAM FORNECIDOS DADOS! ")
        input("TECLE <ENTER>")
    else:
        for k, v in Lista_Todas.items():
            print(f"Código {k} pertence a Sala: {v}")
        print("*** Listagem Pronta ***")
        input("Tecle <Enter>")


# Função para listar elementos das Salas no Dicionário fornecido pelo Usuário:
def ListarElementoLista(armazenamento):
    # recebendo a procura:
    Elemento = input("Digite o que deseja procurar:")
    # variavel que vai indicar se no final não achou:
    achou = False
    if achou:
        # Ver se o Elemento é o procurado
        for Elemento in armazenamento.values():
            if Elemento in armazenamento:
                print("Procura encontrada!")
                print(Elemento)
                achou = True
                input("Tecle <enter>")
    if not achou:
        print("Não encontrei o que procura")
        input("Tecle <enter>")
    print("\n** Procura Finalizada **\n")


# Função de Inclusão de Salas Pronta:
def IncluirSala(armazenamento):  # Inclui Dados da SALA:
    # if opcao == 1,
    # pegando dados da Sala,
    # criando uma lista,
    # armazenando na lista BDSALAS / armazenamento:

    # pegando o Código que vai ser inserindo no dicionário da Sala:
    print("\n*** Incluindo nova Sala ***\n")
    Codigo = str(input("Digite o Código da Sala: "))

    # Testa se já tem o código no dicionário:
    if Codigo in armazenamento:
        print("** Código Existente no Sistema **\n")

    else:
        # cria uma lista vazia:
        DadosSala = []
        # inclusão dos dados na lista:
        Nome = str(input("Digite o nome da Sala: "))
        Capacidade = input("Digite a Capacidade da Sala: ")
        TipoExibicao = input("Digite o Tipo de Exibição da Sala: ")
        Acessibilidade = input("Informe a Acessibilidade da Sala: ")

        # Adiciona os Dados na Lista DadosSala:
        DadosSala.append(Nome)
        DadosSala.append(Capacidade)
        DadosSala.append(TipoExibicao)
        DadosSala.append(Acessibilidade)

        # inclui no dicionario o código e a lista com os dados do código cadastrado:
        armazenamento[Codigo] = DadosSala

        print("\n** Dados inseridos com sucesso!**\n")

        input("Tecle <enter>")


# Falta fazer o código de alteração e arrumar o de exclusão.
def AlterarOuExcluirSalas(armazenamento):
    print(armazenamento)
    armazenado = armazenamento
    dado = str(input(" Digite o que deseja alterar ou excluir: "))
    if dado in armazenado:
        print("\n Para Alterar Digite A ou E para Excluir: \n")
        op = input(" Deseja apagar ou excluir? ").upper
        # op = op.upper()
        while op not in 'AE' or len(op) != 1:
            print(" ERRO!!! opção inválida!! ")
            op = input(" Deseja apagar ou excluir? ")
        if op == 'A':
            print(' Testando! ')
        elif op == 'E':
            del armazenamento[dado]
            print(" Dado Excluido com Sucesso! ")
            input(" TECLE <ENTER>  ")
    else:
        print(" NÃO FOI ENCONTRADO A ENTRADA ESPECIFICADA! ")
        input(" TECLE <ENTER> ")


"""
Funções do menu Sessões
"""

"""
Funções do menu Relatórios
"""
