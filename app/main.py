# Main: Arquivo principal da API, responsável por iniciar, 
# criar as tabelas e registrar os endpoints.

from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import engine, Base
from routers import usuarios, categorias

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Executa tarefas de inicialização antes da API começar a responder requisições
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(
    title="API Achados e Perdidos - GEAF",
    lifespan=lifespan
)

app.include_router(usuarios.router)
app.include_router(categorias.router)