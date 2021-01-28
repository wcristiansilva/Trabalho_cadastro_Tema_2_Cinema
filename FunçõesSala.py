"""
Funções do menu Salas

"""
from FunçõesArquivos import *

# Função para listar todas as Salas no Dicionário:
def ListaTodasSalas(BDSALAS):
    # Lista_Todas = armazenamento
    if len(BDSALAS) == 0:
        print("\n AINDA NÃO FORAM CADASTRADO DADOS! ")
        input("\n TECLE <ENTER>")
    else:
        for sala, dados in BDSALAS.items():
            print(f"\n Código da Sala: {sala} Dados: {dados}", end='')
            # print(f"\n {BDSALAS} \n")
        print("\n\n *** Listagem Pronta ***")
        input("\n TECLE <ENTER> ")


# Função para listar uma Sala do Dicionário fornecido pelo Usuário pelo Código. 
def ListaUmaSalaDici(BDSALAS):
    if len(BDSALAS) == 0:
        print("\n AINDA NÃO FORAM CADASTRADO DADOS! ")
        input("\n TECLE <ENTER>")
    else:
        Procura_lista = int(input("\n Digite o Código da Sala que deseja pesquisar: "))

        if Procura_lista in BDSALAS:
            print(f"\n A Procura retornou a Sala com o Código: {Procura_lista} e seus Dados: {BDSALAS[Procura_lista]}")
        else:
            print("\n Não encontrei o que procura ")
            input("\n TECLE <ENTER> ")
    print("\n ** Procura Finalizada ** ")
    input("\n TECLE <ENTER> ")


# Função de Inclusão de Salas Pronta:
def IncluirSala(armazenamento):
    # if opcao == 1,
    # pegando dados da Sala,
    # criando uma lista,
    # armazenando na lista BDSALAS / armazenamento:

    # pegando o Código que vai ser inserindo no dicionário da Sala:
    print("\n *** Incluindo nova Sala *** ")
    Codigo_Sa = int(input("\n Digite o Código da Sala: "))

    # Testa se já tem o código no dicionário:
    if Codigo_Sa in armazenamento:
        print("\n ** Código Existente no Sistema ** ")
        input("\n TECLE <ENTER> ")

    else:
        # cria uma lista vazia:
        Dados_Sala = []
        # inclusão dos dados na lista:
        Nome = input("Digite o nome da Sala: ")
        Capacidade = input("Digite a Capacidade da Sala: ")
        TipoExibicao = input("Digite o Tipo de Exibição da Sala: ")
        Acessibilidade = input("Informe a Acessibilidade da Sala: ")

        # Adiciona os Dados na Lista Dados_Sala:
        Dados_Sala.append(Nome)
        Dados_Sala.append(Capacidade)
        Dados_Sala.append(TipoExibicao)
        Dados_Sala.append(Acessibilidade)

        # Tranforma a variável com os códigos em tupla pra não serem alterados:

        # inclui no dicionario o código e a lista com os dados do código cadastrado:
        armazenamento[Codigo_Sa] = Dados_Sala

        print("\n ** Dados inseridos com sucesso!** ")

        ArquivoSala(armazenamento)

        input("\n TECLE <ENTER> ")


# Função para Alterar Dados de uma Sala ou Excluir uma Sala inteira ou um Dado passado pelo usuário.
def AlterarOuExcluirSalas(BDSALAS):
    # print(armazenamento) # Usado pra visualizar o dic antes de falzer algo durante os teste
    
    Dado = int(input(" Digite o Código da sala que deseja alterar ou excluir: "))
    if Dado in BDSALAS:
        print("\n Para Alterar Digite A ou E para Excluir: ")
        op = str(input("\n Deseja apagar ou excluir? ")).upper()[0]

        # print(op) # Usado pra ver se a variavel estava recebendo o valor correto durante os teste

        # Recebe a lista do dicionario e faz alteração por indice.
        if op == 'A':
            altera_lista = BDSALAS[Dado]
            print("\nDados da Sala pesquisada abaixo: ")
            print(altera_lista)
            altera_Dado = input("\nO que deseja alterar da sala com base no mostrado acima: ")
            if altera_Dado in altera_lista:
                i = altera_lista.index(altera_Dado)
                novo_dado = input("\nDigite o novo Dado a ser salvo: ")
                altera_lista.pop(i)
                altera_lista.insert(i, novo_dado)
                nova_lista = altera_lista
                BDSALAS[Dado] = nova_lista
                print("\n ** DADO ALTERADO COM SUCESSO **")
                input("\n TECLE <ENTER> ")
            else:
                print(f"\nO {altera_Dado} não consta nos arquivos salvos. \n")
                input("\n TECLE <ENTER> ")

        # Recebe a lista do dicionario e faz a exclusão da Sala toda ou só um dado expecifico por indice.
        elif op == 'E':
            print("\nDeseja deletar todos os dados da Sala ou somente um?")
            escolha_deleta = input("\nDigite T para deletar a Sala toda ou D para somente um Dado especifico: ").upper()[0]           

            if escolha_deleta == 'D':
                deleta_lista = BDSALAS[Dado]
                print("\nDados da Sala pesquisada abaixo: ")
                print(deleta_lista)
                deleta_Dado = input("\nO que deseja deletar da sala com base no mostrado acima: ")
                if deleta_Dado in deleta_lista:
                    i = deleta_lista.index(deleta_Dado)
                    novo_dado = input("\nDigite o novo Dado a ser salvo: ")
                    deleta_lista.pop(i)
                    deleta_lista.insert(i, novo_dado)
                    nova_lista = deleta_lista
                    BDSALAS[Dado] = nova_lista
                    input("\n TECLE <ENTER> ")
                else:
                    print(f"\nO {deleta_Dado} não consta nos arquivos salvos. ")
                    input("\n TECLE <ENTER> ")
            elif escolha_deleta == 'T':
                del BDSALAS[Dado]
                print("\n Dado Excluido com Sucesso! ")
                input("\n TECLE <ENTER>  ")
            
            else:
                print("\n ERRO!!! Opção Inválida!! ")
                input("\n TECLE <ENTER> ")
        else:
            print("\n ERRO!!! Opção Inválida!! ")
            input("\n TECLE <ENTER> ")
    else:
        print("\n NÃO FOI ENCONTRADO O DADO ESPECIFICADO! ")
        input("\n TECLE <ENTER> ")
