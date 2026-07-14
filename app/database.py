import os

# Database: responsável por configurar e gerenciar a conexão da API com o BD 
# utilizando SQLAlchemy

from dotenv import load_dotenv

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession
)
# Importa os recursos do Alchemy 

from sqlalchemy.orm import DeclarativeBase
# Classe base que permite transformar classes Py em tabelas BD.

load_dotenv()
# Carrega as variáveis (.env) para proteger informações (usuário, senhas)

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = (
    f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
) # Monta a URL de conexão pra acessar o Postgres

engine = create_async_engine(DATABASE_URL)

class Base(DeclarativeBase):
    pass

async def get_db_connection():
    return AsyncSession(engine, expire_on_commit=False)
# Sessão de comunicação entre a API e o BD