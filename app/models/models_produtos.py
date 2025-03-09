from typing import List
from pydantic import BaseModel


class ProdutoBase(BaseModel):
    nome: str
    categoria: str
    tags: List[str]


class CriarProduto(ProdutoBase):
    pass


class Produto(ProdutoBase):
    id: int


class HistoricoCompras(BaseModel):
    produtos_ids: List[int]


class Preferencias(BaseModel):
    categorias: List[str] | None = None
    tags: List[str] | None = None
