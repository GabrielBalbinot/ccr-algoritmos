class Tarefa:
    id = None
    descricao = None
    tempo_limite = None
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

def checar_id(lista_de_tarefas, id):

    for tarefa in lista_de_tarefas:

        if tarefa.id == id:
            return True
    
    return False

def remover_tarefa(lista_de_tarefas):

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
            break
    
def concluir_tarefa(lista_de_tarefas):

    print("\tQual o Id da tarefa que deseja marcar como concluída:\n")

    for tarefa in lista_de_tarefas:
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
            break

def visualizar_tarefas(lista_de_tarefas):

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
        
        else:
            print("\tOpção inválida!")
        
        limpar_tela()

menu()

'''
Lista de afazeres para melhorar o trabalho:

1- adicionar comentários nas funções e partes que podem ser confusas;
2- testar mais
3- ver com o professor sobre salvar a lista no computar (manipulação de arquivos) e também sobre usar datas (dates)
4- revisar os tópicos de avaliação
'''
