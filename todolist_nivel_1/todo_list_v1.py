list_todo = []

while True:

    opcao = input("Bem-vindo à To-Do List!\n"
              "1-Adicionar tarefa\n"
              "2-Listar Tarefas\n"
              "3-Sair\n"
              "Escolha uma opção:\n")

    if opcao == '1':
        tarefa = input("Nome tarefa:")
        list_todo.append(tarefa)
    elif opcao == '2':
        if list_todo:
            print("Tarefas:")
            for i, tarefa in enumerate(list_todo, 1):
                print(f"{i}.{tarefa}")
                print("***************")
        else:
            print("Nenhuma tarefa na lista")
            print("*************************")
    elif opcao == '3':
        print("Saindo do sistema...")
        break
    else:
        print("Opção invalida. Tente novamente.")