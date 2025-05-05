from fastapi import APIRouter, HTTPException
from schemas import TarefaBase, TarefaResposta
from services import ListaTarefas
from models import Tarefa
from typing import List

router = APIRouter()
servico = ListaTarefas()

@router.post("/tarefas/", response_model=TarefaResposta)
def criar_tarefa(tarefa: TarefaBase):
    servico.adicionar_tarefa(tarefa)
    return {**tarefa.dict(), "status":"pendente"}

@router.get("/tarefas/", response_model=List[TarefaResposta])
def listar_tarefas():
    tarefas = servico.db.query(Tarefa).all()
    return [TarefaResposta(
        titulo=t.titulo,
        descricao=t.descricao,
        prioridade=t.prioridade,
        status=t.status
    ) for t in tarefas]

@router.delete("/tarefa/{id}")
def remover_tarefa(tarefa_id:int):
    tarefa = servico.db.query(Tarefa).filter(Tarefa.id == tarefa_id).first()
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    servico.db.delete(tarefa)
    servico.db.commit()
    return {"mensagem": "Tarefa removida com sucesso"}

@router.put("/tarefa/{id}")
def concluir_tarefa(tarefa_id:int):
    tarefa = servico.db.query(Tarefa).filter(Tarefa.id == tarefa_id).first()
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    tarefa.status = "concluído"
    servico.db.commit()
    servico.db.refresh(tarefa)
    return {"mensagem": "Tarefa concluída com sucesso"}