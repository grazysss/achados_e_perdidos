from fastapi import APIRouter, HTTPException

import crud
import schemas


router = APIRouter(
    prefix="/locais",
    tags=["Locais"]
)


@router.post("/")
async def criar_local(local: schemas.LocalCreate):

    novo_local = await crud.criar_local(local)

    return {
        "message": "LOCAL CRIADO COM SUCESSO!",
        "local": novo_local
    }


@router.get("/")
async def listar_locais():

    locais = await crud.listar_locais()

    return {
        "message": "LOCAIS LISTADOS COM SUCESSO!",
        "locais": locais
    }


@router.get("/{id}")
async def buscar_local(id: int):

    local = await crud.buscar_local(id)

    if local is None:
        raise HTTPException(
            status_code=404,
            detail="Local não encontrado"
        )

    return {
        "message": "LOCAL ENCONTRADO!",
        "local": local
    }


@router.put("/{id}")
async def atualizar_local(
    id: int,
    local: schemas.LocalCreate
):

    local_atualizado = await crud.atualizar_local(
        id,
        local
    )

    if local_atualizado is None:
        raise HTTPException(
            status_code=404,
            detail="Local não encontrado"
        )

    return {
        "message": "LOCAL ATUALIZADO COM SUCESSO!",
        "local": local_atualizado
    }


@router.delete("/{id}")
async def deletar_local(id: int):

    local_deletado = await crud.deletar_local(id)

    if local_deletado is None:
        raise HTTPException(
            status_code=404,
            detail="Local não encontrado"
        )

    return {
        "message": "LOCAL DELETADO COM SUCESSO!",
        "local": local_deletado
    }