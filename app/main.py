from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import engine, Base
from routers import usuarios, categorias

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(
    title="API Achados e Perdidos - GEAF",
    lifespan=lifespan
)

app.include_router(usuarios.router)
app.include_router(categorias.router)