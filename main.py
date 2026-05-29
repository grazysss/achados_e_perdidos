import asyncpg
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import date

app = FastAPI()

async def get_db_connection():
    return await asyncpg.connect(
        user="postgres",
        password="sql",
        database="achados-e-perdidos",
        host="localhost"
    )

@app.get("/status")
async def status():
    return {"message": "API FUNCIONANDOOO AEEEEEEE!!!"}

@app.get("/test")
async def test_connection():
    conn = await get_db_connection()
    await conn.close()
    return {"message": "Conexão da API_ACHADOS&PERDIDOS com BD_A&P bem-sucedida!"}

@app.get("/items")
async def listar_items():
    conn = await get_db_connection()

    items = await conn.fetch("""
        SELECT * FROM itens """)

    await conn.close()
    return [dict(item) for item in items]

class Item(BaseModel):
    descricao: str
    data_registro: date
    status: str
    dono_recuperou: str | None = None
    categoria_id: int
    local_id: int
    gremista_recebeu_id: int
    gremista_entregou_id: int


@app.post("/items")
async def criar_item(item: Item):
    conn = await get_db_connection()

    novo_item = await conn.fetchrow("""
        INSERT INTO itens (
            descricao,
            data_registro,
            status,
            dono_recuperou,
            categoria_id,
            local_id,
            gremista_recebeu_id,
            gremista_entregou_id
        )
        VALUES ($1, $2, $3, $4, $5, $6, $7, $8)
        RETURNING *
    """,
    item.descricao,
    item.data_registro,
    item.status,
    item.dono_recuperou,
    item.categoria_id,
    item.local_id,
    item.gremista_recebeu_id,
    item.gremista_entregou_id)

    await conn.close()
    return dict(novo_item)


@app.get("/items/{id}")
async def buscar_item(id: int):
    conn = await get_db_connection()

    item = await conn.fetchrow(
        "SELECT * FROM itens WHERE id = $1",
        id
    )

    await conn.close()

    if item is None:
        raise HTTPException(status_code=404, detail="Item não encontrado")

    return dict(item)


@app.put("/items/{id}")
async def atualizar_item(id: int, item: Item):
    conn = await get_db_connection()

    item_atualizado = await conn.fetchrow("""
        UPDATE itens
        SET descricao = $1,
            data_registro = $2,
            status = $3,
            dono_recuperou = $4,
            categoria_id = $5,
            local_id = $6,
            gremista_recebeu_id = $7,
            gremista_entregou_id = $8
        WHERE id = $9
        RETURNING *
    """,
    item.descricao,
    item.data_registro,
    item.status,
    item.dono_recuperou,
    item.categoria_id,
    item.local_id,
    item.gremista_recebeu_id,
    item.gremista_entregou_id,
    id)

    await conn.close()

    if item_atualizado is None:
        raise HTTPException(status_code=404, detail="Item não encontrado")

    return dict(item_atualizado)


@app.delete("/items/{id}")
async def deletar_item(id: int):
    conn = await get_db_connection()

    item_deletado = await conn.fetchrow("""
        DELETE FROM itens
        WHERE id = $1
        RETURNING *
    """, id)

    await conn.close()

    if item_deletado is None:
        raise HTTPException(status_code=404, detail="Item não encontrado")

    return {
        "message": "Item deletado com sucesso",
        "item": dict(item_deletado)
    }