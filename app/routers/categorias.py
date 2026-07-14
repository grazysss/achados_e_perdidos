from fastapi import APIRouter, HTTPException

import crud
import schemas

router = APIRouter(
    prefix="/categorias",
    tags=["Categorias"]
)

@router.post("/", response_model=schemas.CategoriaResponse)
async def criar_categoria(categoria: schemas.CategoriaCreate):
    return await crud.criar_categoria(categoria)

@router.get("/", response_model=list[schemas.CategoriaResponse])
async def listar_categorias():
    return await crud.listar_categorias()

@router.get("/{id}", response_model=schemas.CategoriaResponse)
async def buscar_categoria(id: int):
    categoria = await crud.buscar_categoria(id)

    if categoria is None:
        raise HTTPException(
            status_code=404,
            detail="Categoria não encontrada."
        )
    
    return categoria

@router.put("/{id}", response_model=schemas.CategoriaResponse)
async def atualizar_categoria(id: int, categoria: schemas.CategoriaCreate):
    categoria_atualizada = await crud.atualizar_categoria(id, categoria)

    if categoria_atualizada is None:
        raise HTTPException(
            status_code=404,
            detail="Categoria não encontrada."
        )
    
    return categoria_atualizada

@router.delete("/{id}")
async def deletar_categoria(id: int):
    categoria = await crud.deletar_categoria(id)

    if categoria is None:
        raise HTTPException(
            status_code=404,
            detail="Categoria não encontrada."
        )
    
    return {
        "message": "Categoria deletada com sucesso!"
    }