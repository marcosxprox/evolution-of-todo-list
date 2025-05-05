list_todo = []

def menu():
    print("\nBem-vindo à To-Do List!\n"
          "1 - Adicionar tarefa\n"
          "2 - Listar Tarefas\n"
          "3 - Deletar Tarefa\n"
          "4 - Sair\n")

def criar_tarefa():
    titulo = input("titulo da tarefa:\n")
    descricao = input("descricao da tarefa:\n")
    prioridade = input("prioridade da tarefa:\n")
    tarefa = {'Titulo':titulo, 'Descricao':descricao, 'Prioridade':prioridade}
    list_todo.append(tarefa)
    print(f"Tarefa '{titulo}' adicionada com sucesso!\n")

def listar_tarefas(lista):
    if not lista:
        print("Nenhuma tarefa na lista.\n")
        return
    for i, item in enumerate(lista, 1):
        print("------------------")
        print(f"Tarefa {i}:\nTitulo:{item['Titulo']}\nDescrição:{item['Descricao']}\nPrioridade:{item['Prioridade']}")
        print("------------------")

def deletar_tarefas(lista):

    if not lista:
        print("Não há tarefas para deletar.\n")
        return

    while True:
        try:
            tarefa_indice = int(input("Digite o indice da tarefa que deseja deletar:"))-1
            if 0 <= tarefa_indice < len(lista):
                tarefa_removida = lista.pop(tarefa_indice)
                print(f"A tarefa {tarefa_removida['Titulo']} foi removida")
                break
            else:
                print("Índice inválido. Tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")

while True:

    menu()
    opcao = input("Escolha uma opção:\n")

    if opcao == '1':
        criar_tarefa()

    elif opcao == '2':
        if list_todo:
            listar_tarefas(list_todo)
        else:
            print("Nenhuma tarefa na lista")
            print("*************************")

    elif opcao == '3':
        deletar_tarefas(list_todo)

    elif opcao == '4':
        print("Saindo do sistema...")
        break

    else:
        print("Opção invalida. Tente novamente.")