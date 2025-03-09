from typing import Dict
from fastapi import FastAPI

from app.routers import routers_produtos, routers_usuarios

MESSAGEM_HOME: str = "Bem-vindo à API de Recomendação de Produtos"

app = FastAPI()

app.include_router(routers_usuarios.router)
app.include_router(routers_produtos.router)


@app.get("/")
def home() -> Dict[str, str]:
    global MESSAGEM_HOME
    return {"mensagem": MESSAGEM_HOME}
