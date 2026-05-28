import asyncpg
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

async def get_db_connection():
    return await asyncpg.connect(
        user="postgres",
        password="5432",
        database="achados_e_perdidos",
        host="localhost"
    )

@app.get("/status")
async def status():
    return {"message": "API FUNCIONANDOOO!!!"}

@app.get("/test")
async def test_connection():
    conn = await get_db_connection()
    await conn.close()
    return {"message": "Conexão da API_ACHADOS&PERDIDOS com BD_A&P bem-sucedida!"}