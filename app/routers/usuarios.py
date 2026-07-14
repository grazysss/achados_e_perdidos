from fastapi import APIRouter, HTTPException

import crud
import schemas

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuários"]
)

@router.post("/", response_model=schemas.UsuarioResponse)
async def criar_usuario(usuario: schemas.UsuarioCreate):
    return await crud.criar_usuario(usuario)

@router.get("/", response_model=list[schemas.UsuarioResponse])
async def listar_usuarios():
    return await crud.listar_usuarios()

@router.get("/{id}", response_model=schemas.UsuarioResponse)
async def buscar_usuario(id: int):
    usuario = await crud.buscar_usuario(id)

    if usuario is None:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado."
        )
    
    return usuario

@router.put("/{id}", response_model=schemas.UsuarioResponse)
async def atualizar_usuario(id: int, usuario: schemas.UsuarioCreate):
    usuario_atualizado = await crud.atualizar_usuario(id, usuario)

    if usuario_atualizado is None:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado."
        )
    
    return usuario_atualizado

@router.delete("/{id}")
async def deletar_usuario(id: int):
    usuario = await crud.deletar_usuario(id)

    if usuario is None:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado."
        )
    
    return {
        "message": "Usuário deletado com sucesso!"
    }