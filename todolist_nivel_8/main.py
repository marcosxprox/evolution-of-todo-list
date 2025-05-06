from fastapi import FastAPI
from .routes import router
from fastapi.responses import RedirectResponse

app = FastAPI()
app.include_router(router, prefix="/api")

@app.get("/")
def root():
    return RedirectResponse(url="/docs")
