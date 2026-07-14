from fastapi import APIRouter, HTTPException

import crud
import schemas


router = APIRouter(
    prefix="/itens",
    tags=["Itens"]
)


@router.post("/")
async def criar_item(item: schemas.ItemCreate):

    novo_item = await crud.criar_item(item)

    return {
        "message": "ITEM CRIADO COM SUCESSO!",
        "item": novo_item
    }


@router.get("/")
async def listar_itens():

    itens = await crud.listar_itens()

    return {
        "message": "ITENS LISTADOS COM SUCESSO!",
        "itens": itens
    }


@router.get("/{id}")
async def buscar_item(id: int):

    item = await crud.buscar_item(id)

    if item is None:
        raise HTTPException(
            status_code=404,
            detail="Item não encontrado"
        )

    return {
        "message": "ITEM ENCONTRADO!",
        "item": item
    }


@router.put("/{id}")
async def atualizar_item(
    id: int,
    item: schemas.ItemCreate
):

    item_atualizado = await crud.atualizar_item(
        id,
        item
    )

    if item_atualizado is None:
        raise HTTPException(
            status_code=404,
            detail="Item não encontrado"
        )

    return {
        "message": "ITEM ATUALIZADO COM SUCESSO!",
        "item": item_atualizado
    }


@router.delete("/{id}")
async def deletar_item(id: int):

    item_deletado = await crud.deletar_item(id)

    if item_deletado is None:
        raise HTTPException(
            status_code=404,
            detail="Item não encontrado"
        )

    return {
        "message": "ITEM DELETADO COM SUCESSO!",
        "item": item_deletado
    }