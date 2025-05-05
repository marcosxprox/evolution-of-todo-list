from fastapi import FastAPI
from .routes import router

app = FastAPI()
app.include_router(router, prefix="/api")

@app.get("/")
def root():
    return {"message": "API da To-Do List no ar! Vá para /api/docs"}

