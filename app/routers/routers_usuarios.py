from typing import List
from fastapi import APIRouter

from app.models.models_usuarios import Usuario

router = APIRouter()

usuarios: List[Usuario] = []

contador_usuario: int = 1


@router.post("/usuarios/", response_model=Usuario)
def criarusuario(nome: str) -> Usuario:
    global contador_usuario
    novo_usuario = Usuario(id=contador_usuario, nome=nome)
    usuarios.append(novo_usuario)
    contador_usuario += 1
    return novo_usuario


@router.get("/usuarios/", response_model=List[Usuario])
def listarusuarios() -> List[Usuario]:
    return usuarios
