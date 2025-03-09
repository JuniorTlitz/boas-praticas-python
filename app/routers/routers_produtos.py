from typing import Dict, List
from fastapi import APIRouter, HTTPException

from app.models.models_produtos import (
    CriarProduto,
    HistoricoCompras,
    Preferencias,
    Produto,
)

from .routers_usuarios import usuarios

router = APIRouter()

produtos = List[Produto]
contador_produto: int = 1
historico_de_compras: Dict[int, List[int]] = {}


@router.post("/produtos/", response_model=Produto)
def criarproduto(produto: CriarProduto) -> Produto:
    global contador_produto
    novo_produto = Produto(id=contador_produto, **produto.model_dump())
    produtos.append(novo_produto)
    contador_produto += 1
    return novo_produto


@router.get("/produtos/", response_model=List[Produto])
def listarprodutos() -> List[Produto]:
    return produtos


@router.post("/historico_compras/{usuario_id}")
def adicionarhistoricocompras(
    usuario_id: int, compras: HistoricoCompras
) -> Dict[str, str]:
    if usuario_id not in [usuario.id for usuario in usuarios]:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    historico_de_compras[usuario_id] = compras.produtos_ids
    return {"mensagem": "Histórico de compras atualizado"}


@router.post("/recomendacoes/{usuario_id}", response_model=List[Produto])
def recomendarprodutos(usuario_id: int, preferencias: Preferencias) -> List[Produto]:
    if usuario_id not in historico_de_compras:
        raise HTTPException(
            status_code=404, detail="Histórico de compras não encontrado"
        )

    produtos_recomendados = []

    produtos_recomendados = [
        produto
        for produto_id in historico_de_compras[usuario_id]
        for produto in produtos
        if produto.id == produto_id
    ]

    produtos_recomendados = [
        p for p in produtos_recomendados if p.categoria in preferencias.categorias
    ]
    produtos_recomendados = [
        p
        for p in produtos_recomendados
        if any(tag in preferencias.tags for tag in p.tags)
    ]

    return produtos_recomendados
