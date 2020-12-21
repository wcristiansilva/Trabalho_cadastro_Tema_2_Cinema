"""
Funções do menu Relatórios
"""

def DadosSalasCapacidade(armazenamento):
    
    Data_Dados = armazenamento[1][1]
    if len(armazenamento) == 0:
        print("\n AINDA NÃO FORAM FORNECIDOS DADOS! ")
        input("\n TECLE <ENTER>")
    # armazenamento_lista = list(armazenamento)
    else:
        Capacidade_Procura1 = input("\n Digite a Capacidade inicial desejado: ")
        Capacidade_Procura2 = input("\n Digite a Capacidade final desejada: ")
        for cont in range(len(armazenamento)):
            if Data_Dados[1][1] < Capacidade_Procura1 and Data_Dados[1][1] > Capacidade_Procura2:
                print("Testando")
        '''
        for k, v in armazenamento.items():
            print(f"\n Dados da Sessão {k} Horário da Sessão: {v}")
        print("\n *** Listagem Pronta ***")
        input("\n TECLE <ENTER> ")
        
        '''