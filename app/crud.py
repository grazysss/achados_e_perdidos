from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db_connection

import models
import schemas

async def criar_usuario(usuario: schemas.UsuarioCreate):
    db = await get_db_connection()

    try:
        db_usuario = models.Usuario(
            nome=usuario.nome,
            matricula=usuario.matricula,
            cargo=usuario.cargo,
            username=usuario.username,
            email=usuario.email,
            senha=usuario.senha
        )

        db.add(db_usuario)
        await db.commit()
        await db.refresh(db_usuario)

        return db_usuario

    finally: 
        await db.close()

async def listar_usuarios():
    db = await get_db_connection()

    try:
        result = await db.execute(
            select(models.Usuario)
        )

        usuarios = result.scalars().all()
        return usuarios
    
    finally:
        await db.close()

async def buscar_usuario(id: int):
    db = await get_db_connection()

    try: 
        result = await db.execute(
            select(models.Usuario).where(models.usuario.id == id)
        )

        usuario = result.scalar_one_or_none()
        return usuario

    finally:
        await db.close()

async def atualizar_usuario(id: int, usuario: schemas.UsuarioCreate):
    db = await get_db_connection()

    try:
        result = await db.execute(
            select(models.Usuario).where(models.Usuario.id == id)
        )
        
        db_usuario = result.scalar_one_or_none()

        if db_usuario is None:
            return None
        
        db_usuario.nome = usuario.nome
        db_usuario.matricula = usuario.matricula
        db_usuario.cargo = usuario.cargo
        db_usuario.username = usuario.username
        db_usuario.email = usuario.email
        db_usuario.senha = usuario.senha

        await db.commit()
        await db.refresh(db_usuario)

        return db_usuario
    
    finally:
        await db.close()

async def deletar_usuario(id: int):
    db = await get_db_connection()
    
    try: 
        result = await db.execute(
            select(models.Usuarios).where(models.Usuario.id == id)
        )
    
        db_usuario = result.scalar_one_or_none()

        if db_usuario is None:
            return None
        
        await db.delete(db_usuario)
        await db.commit()

        return db_usuario
    
    finally:
        await db.close()