class Tarefa:
    id = None
    descricao = None
    tempo_limite = None
    # caso essa varíavel seja falsa, significa que a tarefa está ativa
    concluida = False

def adicionar_tarefa(lista_de_tarefas):

    tarefa = Tarefa()

    tarefa.id = int(input("\tDigite um id para a tarefa: "))
    tarefa.descricao = input("\tDescrição da tarefa: ")
    tarefa.tempo_limite = int(input("\tTempo limite (em horas): "))
    print()

    if checar_id(lista_de_tarefas, tarefa.id):
        print("\tJá existe uma tarefa com esse id.")
        print("\tPressione ENTER para voltar ao menu")
        input("\t")
        limpar_tela()
        return

    if tarefa.id <= 0:
        print("\tO id de uma tarefa não pode ser menor ou igual a 0")
        print("\tPressione ENTER para voltar ao menu")
        input("\t")
        limpar_tela()
        return

    lista_de_tarefas.append(tarefa)

    print("\n\tTarefa adicionada com sucesso!")
    print("\tAperte ENTER para voltar ao menu.")
    input("\t")
    limpar_tela()

def ordenar_tarefas(lista_de_tarefas):

    # primeiro é ordenado com base na situação da tarefa:

    for i in range(len(lista_de_tarefas)):

        for j in range(i, len(lista_de_tarefas)):

            if lista_de_tarefas[i].concluida and not lista_de_tarefas[j].concluida:
                temp = lista_de_tarefas[i]
                lista_de_tarefas[i] = lista_de_tarefas[j]
                lista_de_tarefas[j] = temp
    
    # depois é verificado quantas tarefas ativas existem pra fazer a ordenação dessa parte:
    ativos = 0

    for i in range(len(lista_de_tarefas)):
        if lista_de_tarefas[i].concluida:
            break
        ativos += 1

    for i in range(ativos-1):
        for j in range(i+1, ativos):

            if lista_de_tarefas[i].tempo_limite > lista_de_tarefas[j].tempo_limite:
                temp = lista_de_tarefas[i]
                lista_de_tarefas[i] = lista_de_tarefas[j]
                lista_de_tarefas[j] = temp

    # aqui é ordenado com base nas tarefas concluídas:

    for i in range(ativos, len(lista_de_tarefas)):

        for j in range(ativos+1, len(lista_de_tarefas)):
            if lista_de_tarefas[i].tempo_limite > lista_de_tarefas[j].tempo_limite:
                temp = lista_de_tarefas[i]
                lista_de_tarefas[i] = lista_de_tarefas[j]
                lista_de_tarefas[j] = temp        

def checar_id(lista_de_tarefas, id):

    for tarefa in lista_de_tarefas:

        if tarefa.id == id:
            return True
    
    return False

def remover_tarefa(lista_de_tarefas):

    ordenar_tarefas(lista_de_tarefas)
    print("\tQual o Id da tarefa que deseja remover:\n")

    for tarefa in lista_de_tarefas:
        print(f"\t\t{tarefa.id} - {tarefa.descricao}")
    
    print(f"\t\t0 - voltar")

    id = input("\t\t")

    if id == "0":
        return

    for tarefa in lista_de_tarefas:
        if tarefa.id == int(id):
            lista_de_tarefas.remove(tarefa)
            print("\tTarefa removida com sucesso, pressione ENTER para voltar ao menu.")
            input()
            return
    
    print("\tId inválido! Pressione ENTER para voltar ao menu.")
    input()  

def alterar_tarefa(lista_de_tarefas):

    ordenar_tarefas(lista_de_tarefas)

    print("\tQual tarefa deseja alterar?\n")
    for tarefa in lista_de_tarefas:
        print(f"\t\tId: {tarefa.id}")
        print(f"\t\tDescrição: {tarefa.descricao}")
        print(f"\t\tTempo limite: {tarefa.tempo_limite}")
        print()

    id = int(input("\t\t"))

    for tarefa in lista_de_tarefas:
        if tarefa.id == int(id):
            # caso o usuário não deseje alterar alguma propriedade da tarefa, basta pular essa etapa pressionando ENTER, e, 
            # caso deseje concluir dada tarefa, devera utilizar a outra opção do menu
            descricao = input("\n\t\tDigite uma nova descrição (apenas pressione ENTER para não fazer alterações): ")
            tempo_limite = input("\t\tDigite a nova quantidade de tempo limite: (apenas pressione ENTER para não fazer alterações): ")

            if descricao != "":
                tarefa.descricao = descricao
    
            if tempo_limite != "":
                tarefa.tempo_limite = int(tempo_limite)    

            print("\n\tDados alterados com sucesso! Pressione ENTER para voltar ao menu.")
            input()
            return
    
    print("\n\tId inválido! Pressione ENTER para voltar ao menu.")
    input()

def concluir_tarefa(lista_de_tarefas):

    ordenar_tarefas(lista_de_tarefas)

    print("\tQual o Id da tarefa que deseja marcar como concluída:\n")

    for tarefa in lista_de_tarefas:
        if not tarefa.concluida:
            print(f"\t\t{tarefa.id} - {tarefa.descricao}")
    
    print(f"\t\t0 - voltar")

    id = input("\t\t")

    if id == "0":
        return

    for tarefa in lista_de_tarefas:
        if tarefa.id == int(id):
            tarefa.concluida = True
            print("\tTarefa concluída com sucesso, pressione ENTER para voltar ao menu.")
            input()
            return

def reativar_tarefa(lista_de_tarefas):
    
    ordenar_tarefas(lista_de_tarefas)
    print("\tQual o Id da tarefa que deseja reativar:\n")

    for tarefa in lista_de_tarefas:
        if tarefa.concluida:
            print(f"\t\t{tarefa.id} - {tarefa.descricao}")
    
    print(f"\t\t0 - voltar")

    id = input("\t\t")

    if id == "0":
        return

    for tarefa in lista_de_tarefas:
        if tarefa.id == int(id):
            tarefa.concluida = False
            print("\tTarefa reativada com sucesso, pressione ENTER para voltar ao menu.")
            input()
            return

# Essa função pede ao usuário se ele quer filtrar as tarefas que deseja ver,
# após é chamado outra função que imprime as tarefas com ou sem filtragem (ativas ou concluídas)
def visualizar_tarefas(lista_de_tarefas):

    ordenar_tarefas(lista_de_tarefas)
    print("\tDeseja visualizar todas as tarefas, apenas as ativas ou concluídas?")
    print("\tt - Todas")
    print("\ta - Ativas")
    print("\tc - Concluídas")

    escolha = input()

    if escolha == "t":
        visualizar_todas_tarefas(lista_de_tarefas)
    elif escolha == "a":
        visualizar_tarefas_ativas(lista_de_tarefas)
    elif escolha == "c":
        visualizar_tarefas_concluidas(lista_de_tarefas)
    else:
        print("\tEscolha inválida!")
        input("\tPressione ENTER para voltar ao menu.")
    
def visualizar_todas_tarefas(lista_de_tarefas):

    print("\tTarefas adicionadas:\n")

    for tarefa  in lista_de_tarefas:

        print(f"\t\tId: {tarefa.id}")
        print(f"\t\tDescrição: {tarefa.descricao}")
        print(f"\t\tLimite de horas: {tarefa.tempo_limite}")
        print(f"\t\tSituação:", "Concluída" if tarefa.concluida else "Ativa")
        print()

    print("\tPressione ENTER para voltar ao menu.")
    input()
    limpar_tela()

def visualizar_tarefas_ativas(lista_de_tarefas):

    print("\tTarefas ativas:\n")

    for tarefa in lista_de_tarefas:

        if not tarefa.concluida:

            print(f"\t\tId: {tarefa.id}")
            print(f"\t\tDescrição: {tarefa.descricao}")
            print(f"\t\tLimite de horas: {tarefa.tempo_limite}")
            print()

    print("\tPressione ENTER para voltar ao menu.")
    input()
    limpar_tela()

def visualizar_tarefas_concluidas(lista_de_tarefas):

    print("\tTarefas concluídas:\n")

    for tarefa in lista_de_tarefas:

        if tarefa.concluida:

            print(f"\t\tId: {tarefa.id}")
            print(f"\t\tDescrição: {tarefa.descricao}")
            print(f"\t\tLimite de horas: {tarefa.tempo_limite}")
            print(f"\t\tSituação:", "Concluída" if tarefa.concluida else "Ativa")
            print()

    print("\tPressione ENTER para voltar ao menu.")
    input()
    limpar_tela()

def limpar_tela():
    print("\n" * 50)

def menu():
    lista_de_tarefas = []

    while True:

        print("*** Sistema de Gerenciamento de Tarefas ***")
        print("Digite a opção desejada:")
        print("\t0 - Sair")
        print("\t1 - Adicionar tarefa")
        print("\t2 - Concluir tarefa")
        print("\t3 - Remover tarefa")
        print("\t4 - Visualizar tarefas")
        print("\t5 - Alterar tarefa")

        opcao = input("\n\t")

        if opcao == "0":
            break
        
        if opcao == "1":
            adicionar_tarefa(lista_de_tarefas)
        elif opcao == "2":
            concluir_tarefa(lista_de_tarefas)
        elif opcao == "3":
            remover_tarefa(lista_de_tarefas)
        elif opcao == "4":
            visualizar_tarefas(lista_de_tarefas)
        elif opcao == "5":
            alterar_tarefa(lista_de_tarefas)      
        else:
            print("\tOpção inválida!")
            input()
        
        limpar_tela()

menu()

'''
Lista de afazeres para melhorar o trabalho:
adicionar função pra ver tarefas que são concluidas ou não 
1- adicionar comentários nas funções e partes que podem ser confusas;
2- testar mais
3- ver com o professor sobre salvar a lista no computar (manipulação de arquivos) e também sobre usar datas (dates)
4- revisar os tópicos de avaliação
'''
