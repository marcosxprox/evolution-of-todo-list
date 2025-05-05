from pydantic import BaseModel

class TarefaBase(BaseModel):
    titulo:str
    descricao:str
    prioridade:str

class TarefaResposta(TarefaBase):
    status: str

    class Config:
        from_attributes = True