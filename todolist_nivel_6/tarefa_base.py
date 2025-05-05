from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from typing import List
from tarefa import Tarefa
from lista_tarefas import ListaTarefas

app = FastAPI()

class TarefaBase(BaseModel):
    titulo:str
    descricao:str
    prioridade:str

class TarefaResposta(TarefaBase):
    status: str

lista_tarefas = ListaTarefas()

@app.post("/tarefas/", response_model=TarefaResposta)
def adicionar_tarefa(tarefa_data: TarefaBase):
    nova_tarefa = Tarefa(tarefa_data.titulo, tarefa_data.descricao, tarefa_data.prioridade)
    lista_tarefas.adicionar_tarefa(nova_tarefa)
    return nova_tarefa.converter_dict()

@app.get("/tarefas/", response_model=List[TarefaResposta])
def listar_tarefas():
    return [tarefa.converter_dict() for tarefa in lista_tarefas.tarefas]

@app.put("/tarefas/{tarefa_id}/concluir")
def conclui_tarefa(tarefa_id: int):
    try:
        tarefa = lista_tarefas.tarefas[tarefa_id]
        tarefa.concluir()
        return {"message":"tarefa concluída"}
    except IndexError:
        raise HTTPException(status_code=404, detail="tarefa não encontrada")

@app.delete("/tarefas/{tarefa_id}")
def remover_tarefa(tarefa_id: int):
    try:
        tarefa = lista_tarefas.tarefas.pop(tarefa_id)
        return {"message": f"Tarefa '{tarefa.titulo}' removida"}
    except IndexError:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)