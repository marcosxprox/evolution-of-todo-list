class Tarefa:

    def __init__(self, titulo, descricao, prioridade, status = "pendente"):
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.status = status

    def concluir(self):
        if self.status == "pendente":
           self.status = "concluído"
        return self.status

    def __str__(self):
        return (f"Titulo: {self.titulo}\n"
                f"Descrição: {self.descricao}\n"
                f"Prioridade: {self.prioridade}\n"
                f"Status: {self.status}")







