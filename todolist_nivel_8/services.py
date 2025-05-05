import json
from .schemas import TarefaBase
from .models import Tarefa, SessionLocal

class ListaTarefas:

    def __init__(self):
        self.db = SessionLocal()

    def adicionar_tarefa(self, tarefa_data: TarefaBase):
        tarefa = Tarefa(titulo = tarefa_data.titulo, descricao = tarefa_data.descricao, prioridade = tarefa_data.prioridade)
        self.db.add(tarefa)
        self.db.commit()
        self.db.refresh(tarefa)
        print("Tarefa adicionada com sucesso!")

    def remover_tarefa(self, indice:int):
        tarefa = self.db.query(Tarefa).filter(Tarefa.id == indice).first()
        if tarefa:
            self.db.delete(tarefa)
            self.db.commit()
            print("Tarefa removida com sucesso!")

    def listar_tarefas(self):
        tarefas = self.db.query(Tarefa).all()
        for tarefa in tarefas:
            print(f"ID:{tarefa.id},\nTitulo:{tarefa.titulo},\nDescrição:{tarefa.descricao},"
                  f"\nPrioridade:{tarefa.prioridade},\nStatus:{tarefa.status}")

    def concluir_tarefa(self, indice: int):
       tarefa = self.db.query(Tarefa).filter(Tarefa.id == indice).first()
       if tarefa:
           tarefa.status = "concluído"
           self.db.commit()
           self.db.refresh(tarefa)
           print("Tarefa Concluída com sucesso")
       else:
           print("Tarefa não encontrada")

    def salvar_em_arquivo(self, nome_arquivo):
        with open(nome_arquivo, "w", encoding="utf-8") as arq:
            tarefas = self.db.query(Tarefa).all()
            json.dump([t.converter_dict() for t in tarefas], arq, indent=4)# type: ignore

    def carregar_tarefas(self, nome_arquivo):
        try:
            with open(nome_arquivo, "r", encoding="utf-8") as arq:
                dados = json.load(arq)
                for item in dados:
                    exist = self.db.query(Tarefa).filter_by(titulo=item['titulo'], descricao=item['descricao']).first()
                    if not exist:
                        tarefa = Tarefa(**item)
                        self.db.add(tarefa)
                self.db.commit()
                print("Tarefas carregadas com sucesso!")
        except FileNotFoundError:
            pass