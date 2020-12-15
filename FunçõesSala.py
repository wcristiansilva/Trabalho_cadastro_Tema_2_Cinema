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


# Função para listar elementos das Salas no Dicionário fornecido pelo Usuário: falta corrigir a procura dentro do dicionario. procurar  a sala e mostrar os elementos da mesma 
def ListarElementoLista(armazenamento):
    # recebendo a procura:
    Elemento = input("Digite o que deseja procurar:")
    # variavel que vai indicar se no final não achou:
    achou = True
    # Ver se o Elemento é o procurado
    if achou:
        for Elemento in armazenamento:
            if Elemento in armazenamento:
                print("\nProcura Finalizada!")
                print(Elemento)
                # achou = True
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


# Falta fazer o código de alteração e arrumar o de exclusão onde precisa saber se vai excluir só algum dado ou o par chave/valor.
def AlterarOuExcluirSalas(armazenamento):
    print(armazenamento) # Usado pra visualizar o dic antes de falzer algo
    
    Dado = input(" Digite o que dado que deseja alterar ou excluir: ")
    if Dado in armazenamento:
        print("\n Para Alterar Digite A ou E para Excluir: ")
        op = str(input("\n Deseja apagar ou excluir? "))
        op = op.upper()

        print(op) # Usado pra ver se a variavel estava recebendo o valor correto

        if op == 'A':
            print('\n Testando! ')
        
        # Deleta a chave mais os valores passado encontrado no dic
        elif op == 'E':
            del armazenamento[Dado]
            print("\n Dado Excluido com Sucesso! ")
            input("\n TECLE <ENTER>  ")
        else:
            print("\n ERRO!!! Opção Inválida!! ")
    else:
        print("\n NÃO FOI ENCONTRADO O DADO ESPECIFICADO! ")
        input("\n TECLE <ENTER> ")


"""
Funções do menu Sessões
"""

"""
Funções do menu Relatórios
"""
