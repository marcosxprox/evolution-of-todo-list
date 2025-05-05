from fastapi.testclient import TestClient
from tarefa_base import app

cliente = TestClient(app)

def test_adicionar_tarefa():
    response = cliente.post("/tarefas/", json = {"titulo":"Correr", "descricao":"corrida de 10 voltas", "prioridade":"alta"})
    assert response.status_code==200
    assert response.json()["titulo"]=="Correr"
    assert response.json()["descricao"]=="corrida de 10 voltas"
    assert response.json()["prioridade"]=="alta"

def test_listar_tarefas():
    response = cliente.get("/tarefas/")
    assert response.status_code==200
    assert len(response.json()) > 0

def test_conclui_tarefa():
    response = cliente.post("/tarefas/",
               json={"titulo": "Correr", "descricao": "corrida de 10 voltas", "prioridade": "alta"})
    assert response.status_code==200
    tarefa_id = 0
    response = cliente.put(f"/tarefas/{tarefa_id}/concluir")
    assert response.status_code==200
    assert response.json()["message"] == "tarefa concluída"

def test_remover_tarefa():
    response = cliente.post("/tarefas/",
               json={"titulo": "Correr", "descricao": "corrida de 10 voltas", "prioridade": "alta"})
    assert response.status_code==200
    tarefa_id = 0
    response = cliente.delete(f"/tarefas/{tarefa_id}")
    assert "removida" in response.json()["message"]