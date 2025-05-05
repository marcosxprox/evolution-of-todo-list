from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Tarefa(Base):
    __tablename__ = 'tarefas'

    id = Column(Integer, primary_key = True, autoincrement = True)
    titulo = Column(String, nullable=False)
    descricao = Column(String, nullable=False)
    prioridade = Column(String, nullable=False)
    status = Column(String, default="pendente")

    def converter_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "prioridade": self.prioridade,
            "status": self.status
        }

DATABASE_URL = "sqlite:///./tarefas.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread":False})
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

