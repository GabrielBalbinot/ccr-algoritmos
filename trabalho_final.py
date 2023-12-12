class Tarefa:
    id = None
    descricao = None
    tempo_limite = None
    # caso essa varíavel seja falsa, significa que a tarefa está ativa
    concluida = False

def adicionar_tarefa(lista_de_tarefas):

    tarefa = Tarefa()

    tarefa.id = int(input("\t\tDigite um id para a tarefa: "))
    tarefa.descricao = input("\t\tDescrição da tarefa: ")
    tarefa.tempo_limite = int(input("\t\tTempo limite (em horas): "))
    print()

    if checar_id(lista_de_tarefas, tarefa.id):
        print("\t\tJá existe uma tarefa com esse id.")
        print("\t\tPressione ENTER para voltar ao menu")
        input("\t")
        limpar_tela()
        return

    if tarefa.id <= 0:
        print("\t\tO id de uma tarefa não pode ser menor ou igual a 0")
        print("\t\tPressione ENTER para voltar ao menu")
        input("\t\t")
        limpar_tela()
        return

    lista_de_tarefas.append(tarefa)

    print("\t\tTarefa adicionada com sucesso!")
    print("\t\tAperte ENTER para voltar ao menu.")
    input("\t\t")
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
    print("\t\tQual o id da tarefa que deseja remover:\n")

    for tarefa in lista_de_tarefas:
        print(f"\t\t\t{tarefa.id} - {tarefa.descricao}")
    
    print(f"\t\t0\t - voltar")

    id = input("\t\t\t")

    if id == "0":
        return

    for tarefa in lista_de_tarefas:
        if tarefa.id == int(id):
            lista_de_tarefas.remove(tarefa)
            print("\t\tTarefa removida com sucesso, pressione ENTER para voltar ao menu.")
            input()
            return
    
    print("\t\tId inválido! Pressione ENTER para voltar ao menu.")
    input()  

def alterar_tarefa(lista_de_tarefas):

    ordenar_tarefas(lista_de_tarefas)

    print("\t\tQual tarefa deseja alterar?\n")
    for tarefa in lista_de_tarefas:
        print(f"\t\t\tId: {tarefa.id}")
        print(f"\t\t\tDescrição: {tarefa.descricao}")
        print(f"\t\t\tTempo limite: {tarefa.tempo_limite}")

    id = int(input("\n\t\t\t"))

    for tarefa in lista_de_tarefas:
        if tarefa.id == int(id):
            # caso o usuário não deseje alterar alguma propriedade da tarefa, basta pular essa etapa pressionando ENTER, e, 
            # caso deseje concluir dada tarefa, devera utilizar a outra opção do menu
            descricao = input("\n\t\t\tDigite uma nova descrição (apenas pressione ENTER para não fazer alterações): ")
            tempo_limite = input("\t\t\tDigite a nova quantidade de tempo limite: (apenas pressione ENTER para não fazer alterações): ")

            if descricao != "":
                tarefa.descricao = descricao
    
            if tempo_limite != "":
                tarefa.tempo_limite = int(tempo_limite)    

            print("\n\t\tDados alterados com sucesso! Pressione ENTER para voltar ao menu.")
            input("\n\t\t")
            return
    
    print("\n\tId inválido! Pressione ENTER para voltar ao menu.")
    input()

def concluir_tarefa(lista_de_tarefas):

    ordenar_tarefas(lista_de_tarefas)

    print("\t\tQual o Id da tarefa que deseja marcar como concluída:\n")

    for tarefa in lista_de_tarefas:
        if not tarefa.concluida:
            print(f"\t\t\t{tarefa.id} - {tarefa.descricao}")
    
    print(f"\t\t\t0 - voltar")

    id = input("\n\t\t\t")

    if id == "0":
        return

    for tarefa in lista_de_tarefas:
        if tarefa.id == int(id):
            tarefa.concluida = True
            print("\n\t\tTarefa concluída com sucesso, pressione ENTER para voltar ao menu.")
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
    print("\t\t\tDeseja visualizar todas as tarefas, apenas as ativas ou concluídas?")
    print("\t\t\t\tt - Todas")
    print("\t\t\t\ta - Ativas")
    print("\t\t\t\tc - Concluídas")

    escolha = input("\n\t\t\t\t")

    if escolha == "t":
        visualizar_todas_tarefas(lista_de_tarefas)
    elif escolha == "a":
        visualizar_tarefas_ativas(lista_de_tarefas)
    elif escolha == "c":
        visualizar_tarefas_concluidas(lista_de_tarefas)
    else:
        print("\n\t\t\tEscolha inválida!")
        input("\t\t\tPressione ENTER para voltar ao menu.")
    
def visualizar_todas_tarefas(lista_de_tarefas):

    print("\n\t\t\t\tTarefas adicionadas:\n")

    for tarefa  in lista_de_tarefas:

        print(f"\t\t\t\t\tId: {tarefa.id}")
        print(f"\t\t\t\t\tDescrição: {tarefa.descricao}")
        print(f"\t\t\t\t\tLimite de horas: {tarefa.tempo_limite}")
        print(f"\t\t\t\t\tSituação:", "Concluída" if tarefa.concluida else "Ativa")
        print()

    print("\t\t\t\tPressione ENTER para voltar ao menu.")
    input("\t\t\t\t")
    limpar_tela()

def visualizar_tarefas_ativas(lista_de_tarefas):

    print("\n\t\t\t\tTarefas ativas:\n")

    for tarefa in lista_de_tarefas:

        if not tarefa.concluida:

            print(f"\t\t\t\t\tId: {tarefa.id}")
            print(f"\t\t\t\t\tDescrição: {tarefa.descricao}")
            print(f"\t\t\t\t\tLimite de horas: {tarefa.tempo_limite}")
            print()

    print("\t\t\t\tPressione ENTER para voltar ao menu.")
    input("\t\t\t\t")
    limpar_tela()

def visualizar_tarefas_concluidas(lista_de_tarefas):

    print("\n\t\t\t\tTarefas concluídas:\n")

    for tarefa in lista_de_tarefas:

        if tarefa.concluida:

            print(f"\t\t\t\t\tId: {tarefa.id}")
            print(f"\t\t\t\t\tDescrição: {tarefa.descricao}")
            print(f"\t\t\t\t\tLimite de horas: {tarefa.tempo_limite}")
            print()

    print("\t\t\t\tPressione ENTER para voltar ao menu.")
    input("\t\t\t")
    limpar_tela()

def limpar_tela():
    import os
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")
        #print("\n" * 10)

def salvar_arquivo(lista_de_tarefas, caminho):

    # Essa função salva cada tarefa num documento .txt no caminho informado pelo usuário.
    # O formato que será salvo é: Id: int|Descrição: str|Tempo Limite: int|Situação: bool

    import os

    if caminho == '':
        print("\tArquivo não salvo pois não foi passado nenhum caminho.")
        return True
    
    if not os.path.exists(caminho):
        print("\tCaminho não encontrado.")
        return False

    ordenar_tarefas(lista_de_tarefas)


    with open(caminho, "w") as arquivo:
        for tarefa in lista_de_tarefas:
            # A situação da tarefa, no programa foi salva como bool, porém ao escrever no arquivo dessa forma (True ou False),
            # um posterior carregamento do arquivo fará com que todas sejam marcadas como True, ou seja, como concluídas.
            # Isso se dá devido a como o python tratá booleanos: qualquer coisa diferente de 0 é tratado como True, enquanto 0 é False
            linha = f"{tarefa.id}|{tarefa.descricao}|{tarefa.tempo_limite}|{int(tarefa.concluida)}\n"
            arquivo.write(linha)
    
    return True

def carregar_arquivo(caminho):

    # Essa função pega um arquivo e faz a leitura e posteriormente retorna uma lista com as tarefas, caso esteja no formato certo

    import os

    lista = []

    if not os.path.exists(caminho):
        print("\t\tCaminho não encontrado! Pressione ENTER para voltar ao menu.")
        input("\t\t")
        return
    
    with open(caminho, 'r') as arquivo:
        
        for linha in arquivo:
            tarefa = Tarefa()

            # Aqui é feito a leitura da linha e divida a cada barra lateral (|)
            linha_div = linha.strip().split("|")

            tarefa.id = int(linha_div[0])
            tarefa.descricao = linha_div[1]
            tarefa.tempo_limite = linha_div[2]
            # Aqui é transformado em int primeiramente, após é transformado em booleano e salvo no atributo da variável tarefa
            tarefa.concluida = bool(int(linha_div[3]))

            lista.append(tarefa)
    
    input("\t\tDados carregados com sucesso! Pressione ENTER para voltar ao menu.")
    return lista

def menu():
    lista_de_tarefas = []

    while True:

        print("*** Sistema de Gerenciamento de Tarefas ***\n")
        print("\tDigite a opção desejada:")
        print("\t\t0 - Sair")
        print("\t\t1 - Adicionar tarefa")
        print("\t\t2 - Concluir tarefa")
        print("\t\t3 - Remover tarefa")
        print("\t\t4 - Visualizar tarefas")
        print("\t\t5 - Alterar tarefa")
        print("\t\t6 - Carregar arquivo")

        opcao = input("\n\t\t")
        print()

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
        elif opcao == "6":
            caminho = input("\t\tDigite o caminho do arquivo: ")
            lista_de_tarefas = carregar_arquivo(caminho)      
        else:
            print("\tOpção inválida!")
            input()
        
        limpar_tela()
    

    caminho = input("\tCaso deseje salvar a lista de tarefas, digite o caminho para o arquivo, caso contrário pressione ENTER: ")

    while not salvar_arquivo(lista_de_tarefas, caminho):
        caminho = input("\n\tPor favor digite o caminho corretamente ou pressione ENTER para fechar o programa sem salvar as tarefas: ")

    input()

    #salvar_arquivo(lista_de_tarefas, caminho)

menu()

'''
Lista de afazeres para melhorar o trabalho:
adicionar função pra ver tarefas que são concluidas ou não 
1- adicionar comentários nas funções e partes que podem ser confusas;
2- testar mais
3- ver com o professor sobre salvar a lista no computar (manipulação de arquivos) e também sobre usar datas (dates)
4- revisar os tópicos de avaliação
'''
