class ListaTarefas:

    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def remover_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            confirmacao = input("Tem certeza que deseja remover? (s/n): ")
            if confirmacao.lower() == 's':
                del self.tarefas[indice]
        else:
            print("Índice inválido.")

    def listar_tarefas(self):

        if not self.tarefas:
            print("Nenhuma tarefa cadastrada.")
            return

        for i, tarefa in enumerate(self.tarefas):
            print(f"Tarefa {i}:")
            print(tarefa)

    def concluir_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice].concluir()
        else:
            print("indice invalido.")
