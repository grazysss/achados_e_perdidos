# Crud: Contém toda lógica de acesso ao BD realizando todas as operações
# (POST, GET, PUT, DELETE)

from sqlalchemy import select
from database import get_db_connection

import models
import schemas
from auth import hash_password, verify_password

# CRUD USUÁRIOS

async def criar_usuario(usuario: schemas.UsuarioCreate):
    db = await get_db_connection()
    
    try:
        db_usuario = models.Usuario(
            nome=usuario.nome,
            matricula=usuario.matricula,
            cargo=usuario.cargo,
            username=usuario.username,
            email=usuario.email,
            senha=hash_password(usuario.senha)
        )

        db.add(db_usuario) # Adiciona o obj à sessão do BD
        await db.commit() # Confirma as alterações no BD
        await db.refresh(db_usuario) # Atualiza o objeto com suas novas informações

        return db_usuario

    finally: 
        await db.close()



async def listar_usuarios():
    db = await get_db_connection()

    try:
        result = await db.execute( # Executa uma consulta
            select(models.Usuario) # Seleciona registros de uma tabela
        )

        usuarios = result.scalars().all()
        return usuarios
    
    finally:
        await db.close()

async def buscar_usuario(id: int):
    db = await get_db_connection()

    try: 
        result = await db.execute(
            select(models.Usuario).where(models.Usuario.id == id)
        )

        usuario = result.scalar_one_or_none()
        return usuario

    finally:
        await db.close()

async def buscar_usuario_username(username: str):
    db = await get_db_connection()

    try:
        result = await db.execute(
            select(models.Usuario).where(
                models.Usuario.username == username
            )
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
        db_usuario.senha = hash_password(usuario.senha)

        await db.commit()
        await db.refresh(db_usuario)

        return db_usuario
    
    finally:
        await db.close()

async def deletar_usuario(id: int):
    db = await get_db_connection()
    
    try: 
        result = await db.execute(
            select(models.Usuario).where(models.Usuario.id == id)
        )
    
        db_usuario = result.scalar_one_or_none()

        if db_usuario is None:
            return None
        
        await db.delete(db_usuario)
        await db.commit()

        return db_usuario
    
    finally:
        await db.close()

# CRUD CATEGORIAS
async def criar_categoria(categoria: schemas.CategoriaCreate):
    db = await get_db_connection()

    try:
        db_categoria = models.Categoria(
            nome_categoria=categoria.nome_categoria
        )

        db.add(db_categoria)

        await db.commit()
        await db.refresh(db_categoria)

        return db_categoria
    
    finally:
        await db.close()

async def listar_categorias():
    db = await get_db_connection()

    try: 
        result = await db.execute(
            select(models.Categoria)
        )

        return result.scalars().all()
    
    finally:
        await db.close()

async def buscar_categoria(id: int):
    db = await get_db_connection()

    try:
        result = await db.execute(
            select(models.Categoria).where(models.Categoria.id == id)
        )

        return result.scalar_one_or_none() 
    
    finally:
        await db.close()

async def atualizar_categoria(id: int, categoria: schemas.CategoriaCreate):
    db = await get_db_connection()

    try:
        result = await db.execute(
            select(models.Categoria).where(models.Categoria.id == id)
        )

        db_categoria = result.scalar_one_or_none()

        if db_categoria is None:
            return None
        
        db_categoria.nome_categoria = categoria.nome_categoria

        await db.commit()
        await db.refresh(db_categoria)

        return db_categoria

    finally:
        await db.close()   

async def deletar_categoria(id: int):
    db = await get_db_connection()

    try:
        result = await db.execute(
            select(models.Categoria).where(models.Categoria.id == id)
        )

        db_categoria = result.scalar_one_or_none()

        if db_categoria is None:
            return None
        
        await db.delete(db_categoria)
        await db.commit()
        
        return db_categoria
    
    finally: 
        await db.close()

# CRUD LOCAIS

async def criar_local(local: schemas.LocalCreate):
    db = await get_db_connection()

    try:
        db_local = models.Local(
            nome_local=local.nome_local,
            bloco=local.bloco
        )

        db.add(db_local)

        await db.commit()
        await db.refresh(db_local)

        return db_local

    finally:
        await db.close()


async def listar_locais():
    db = await get_db_connection()

    try:
        result = await db.execute(
            select(models.Local)
        )

        return result.scalars().all()

    finally:
        await db.close()


async def buscar_local(id: int):
    db = await get_db_connection()

    try:
        result = await db.execute(
            select(models.Local)
            .where(models.Local.id == id)
        )

        return result.scalar_one_or_none()

    finally:
        await db.close()


async def atualizar_local(id: int, local: schemas.LocalCreate):
    db = await get_db_connection()

    try:
        result = await db.execute(
            select(models.Local)
            .where(models.Local.id == id)
        )

        db_local = result.scalar_one_or_none()

        if db_local is None:
            return None

        db_local.nome_local = local.nome_local
        db_local.bloco = local.bloco

        await db.commit()
        await db.refresh(db_local)

        return db_local

    finally:
        await db.close()


async def deletar_local(id:int):
    db = await get_db_connection()

    try:
        result = await db.execute(
            select(models.Local)
            .where(models.Local.id == id)
        )

        db_local = result.scalar_one_or_none()

        if db_local is None:
            return None

        await db.delete(db_local)
        await db.commit()

        return db_local

    finally:
        await db.close()