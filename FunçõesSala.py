"""
Funções do menu Salas
"""


# Função para listar todas as Salas no Dicionário:
def ListaTodasSalas(armazenamento):
    # Lista_Todas = armazenamento
    if len(armazenamento) == 0:
        print("\nAINDA NÃO FORAM FORNECIDOS DADOS! ")
        input("\nTECLE <ENTER>")
    else:
        for k, v in armazenamento.items():
            print(f"Código {k} pertence a Sala: {v}")
        print("\n*** Listagem Pronta ***")
        input("\nTecle <Enter>")


# Função para listar elementos das Salas no Dicionário fornecido pelo Usuário: falta corrigir a procura dentro do dicionario.
def ListarElementoLista(armazenamento):
    # recebendo a procura:
    Elemento = input("Digite o que deseja procurar:")
    # variavel que vai indicar se no final não achou:
    achou = False
    # Ver se o Elemento é o procurado
    for Elemento in armazenamento:
        if Elemento in armazenamento:
            print("\nProcura encontrada!")
            print(Elemento)
            achou = True
            input("\nTecle <enter>")
    if not achou:
        print("\nNão encontrei o que procura")
        input("\nTecle <enter>")
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
    Dado = input(" Digite o que dado que deseja alterar ou excluir: ")
    if Dado in armazenado:
        print("\n Para Alterar Digite A ou E para Excluir: \n")
        op = input(" Deseja apagar ou excluir? ").upper
        while op != 'A' or op != 'E':
            print(" ERRO!!! opção inválida!! ")
            op = input(" Deseja apagar ou excluir? ").upper
            
        if op == 'A':
            print(' Testando! ')
        elif op == 'E':
            del armazenamento[Dado]
            print(" Dado Excluido com Sucesso! ")
            input(" TECLE <ENTER>  ")
    else:
        print(" NÃO FOI ENCONTRADO O DADO ESPECIFICADO! ")
        input(" TECLE <ENTER> ")


"""
Funções do menu Sessões
"""

"""
Funções do menu Relatórios
"""
