from schemas import TarefaBase
from services import ListaTarefas
from fastapi import FastAPI
from routes import router

app = FastAPI()
app.include_router(router, prefix="/api")

def menu():
    print("\nBem-vindo à To-Do List!\n"
          "1 - Adicionar tarefa\n"
          "2 - Listar tarefas\n"
          "3 - Deletar tarefa\n"
          "4 - Concluir tarefa\n"
          "5 - Sair\n")

def criar_tarefa():
    titulo = input("Titulo da tarefa: ")
    descricao = input("Descricao da tarefa: ")
    while True:
        prioridade = input("Prioridade tarefa 'alta', 'media' ou 'baixa': ")
        if validar_prioridade(prioridade):
            break
    return TarefaBase(titulo=titulo, descricao=descricao, prioridade=prioridade.lower())

def validar_prioridade(prioridade):
    prioridades = ['alta', 'media', 'baixa']
    if prioridade.lower() not in prioridades:
        print("Erro: prioridade so pode ser 'alta', 'media', 'baixa'")
        return False
    return True

lista = ListaTarefas()
lista.carregar_tarefas("lista.json")

if __name__ == "__main__":

    while True:

        menu()
        opcao = input("Escolha uma opção:\n")

        if opcao == '1':
            tarefa_data = criar_tarefa()
            lista.adicionar_tarefa(tarefa_data)
            lista.salvar_em_arquivo("lista.json")

        elif opcao == '2':
            lista.listar_tarefas()

        elif opcao == '3':
            try:
                indice = int(input("Digite o indice da tarefa que deseja remover:"))
                lista.remover_tarefa(indice)
                lista.salvar_em_arquivo("lista.json")
                print("Tarefa removida com sucesso!")
            except ValueError:
                print("Por favor, insira um número válido.")

        elif opcao == '4':
            try:
                indice = int(input("Digite o indice da tarefa que deseja concluir:"))
                lista.concluir_tarefa(indice)
                lista.salvar_em_arquivo("lista.json")
            except ValueError:
                print("Por favor, insira um número válido.")

        elif opcao == '5':
            print("Saindo do sistema...")
            break

        else:
            print("Opção invalida. Tente novamente.")
