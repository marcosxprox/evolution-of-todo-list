from tarefa import Tarefa
from lista_tarefas import ListaTarefas

def menu():
    print("\nBem-vindo à To-Do List!\n"
          "1 - Adicionar tarefa\n"
          "2 - Listar tarefas\n"
          "3 - Deletar tarefa\n"
          "4 - Concluir tarefa\n"
          "5 - Sair\n")

def criar_tarefa():
    titulo = input("Titulo da tarefa:")
    descricao = input("Descricao da tarefa:")
    prioridade = input("Prioridade tarefa:")
    return Tarefa(titulo, descricao, prioridade)

lista = ListaTarefas()

if __name__ == "__main__":

    while True:

        menu()
        opcao = input("Escolha uma opção:\n")

        if opcao == '1':
            tarefa = criar_tarefa()
            lista.adicionar_tarefa(tarefa)

        elif opcao == '2':
            lista.listar_tarefas()

        elif opcao == '3':
            try:
                indice = int(input("Digite o indice da tarefa que deseja remover:"))
                lista.remover_tarefa(indice)
                print("Tarefa removida com sucesso!")
            except ValueError:
                print("Por favor, insira um número válido.")

        elif opcao == '4':
            try:
                indice = int(input("Digite o indice da tarefa que deseja concluir:"))
                lista.concluir_tarefa(indice)
                print("Tarefa concluída com sucesso!")
            except ValueError:
                print("Por favor, insira um número válido.")

        elif opcao == '5':
            print("Saindo do sistema...")
            break

        else:
            print("Opção invalida. Tente novamente.")
