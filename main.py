import asyncpg
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import date

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
    return {"message": "API FUNCIONANDOOO AEEEEEEE!!!"}

@app.get("/test")
async def test_connection():
    conn = await get_db_connection()
    await conn.close()
    return {"message": "Conexão da API_ACHADOS&PERDIDOS com BD_A&P bem-sucedida!"}

@app.get("/itens")
async def listar_itens():
    conn = await get_db_connection()
    itens = await conn.fetch("""
        SELECT
            i.id,
            i.descricao,
            i.data_registro,
            i.status,
            i.dono_recuperou,
            c.nome_categoria,
            l.nome_local,
            l.bloco,
            gr.nome AS gremista_recebeu_nome,
            ge.nome AS gremista_entregou_nome
        FROM itens i
        JOIN categorias c ON i.categoria_id = c.id
        JOIN locais l ON i.local_id = l.id
        JOIN gremistas gr ON i.gremista_recebeu_id = gr.id
        JOIN gremistas ge ON i.gremista_entregou_id = ge.id
        ORDER BY i.id
    """)
    await conn.close()

    list_itens = []
    for i in itens:
        list_itens.append({
                "id": i["id"],
                "descricao": i["descricao"],
                "data_registro": str(i["data_registro"]),
                "status": i["status"],
                "dono_recuperou": i["dono_recuperou"],
                "categoria": i["nome_categoria"],
                "local": i["nome_local"],
                "bloco": i["bloco"],
                "gremista_recebeu": i["gremista_recebeu_nome"],
                "gremista_entregou": i["gremista_entregou_nome"]
            })
    return {"item": list_itens}


# @app.get("/get_alunos")
# async def get_alunos():
#     conn = await get_db_connection()
#     alunos = await conn.fetch("SELECT * FROM alunos")
#     await conn.close()

#     list_alunos = []
#     for i in alunos:
#         list_alunos.append(f"ID do aluno: {i["id"]}, nome: {i["nome"]}, email: {i["email"]}")
#     return {"users": list_alunos}

class Item(BaseModel):
    descricao: str
    data_registro: date
    status: str
    dono_recuperou: str | None = None
    categoria_id: int
    local_id: int
    gremista_recebeu_id: int
    gremista_entregou_id: int


@app.post("/itens")
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
    """,
    item.descricao,
    item.data_registro,
    item.status,
    item.dono_recuperou,
    item.categoria_id,
    item.local_id,
    item.gremista_recebeu_id,
    item.gremista_entregou_id
    )

    await conn.close()
    return {"message": "ITEM CRIADO!"}

@app.get("/itens/{id}")
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


@app.put("/itens/{id}")
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


@app.delete("/itens/{id}")
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