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

class Gremista(BaseModel):
    nome: str
    matricula: str
    cargo: str

class Categoria(BaseModel):
    nome_categoria: str

class Local(BaseModel):
    nome_local: str
    bloco: str
class Item(BaseModel):
    descricao: str
    data_registro: date
    status: str
    dono_recuperou: str | None = None
    categoria_id: int
    local_id: int
    gremista_recebeu_id: int
    gremista_entregou_id: int | None = None

@app.get("/status")
async def status():
    return {"message": "API FUNCIONANDOOO AEEEEEEE!!!"}

@app.get("/test")
async def test_connection():
    conn = await get_db_connection()
    await conn.close()
    return {"message": "Conexão da API_ACHADOS&PERDIDOS com BD_A&P bem-sucedida!"}

@app.post("/gremistas")
async def adicionar_gremista(gremistas: Gremista):
    conn = await get_db_connection()
    novo_gremista = await conn.fetchrow("""
        INSERT INTO gremistas (nome, matricula, cargo)
        VALUES ($1, $2, $3)
        RETURNING *
        """,
        gremistas.nome,
        gremistas.matricula,
        gremistas.cargo
        )
    
    await conn.close()
    return {
        "message": "GREMISTA ADICIONADO COM SUCESSO!!",
        "gremista": dict(novo_gremista)
    }

@app.get("/gremistas")
async def listar_gremistas():
    conn = await get_db_connection()

    gremistas = await conn.fetch("""
        SELECT * FROM gremistas
        ORDER BY id
    """)

    await conn.close()

    return {
        "message": "GREMISTAS LISTADOS COM SUCESSO!",
        "gremistas": [dict(gremista) for gremista in gremistas]
    }

@app.delete("/gremistas/{id}")
async def deletar_gremista(id: int):
    conn = await get_db_connection()

    gremista_deletado = await conn.fetchrow("""
        DELETE FROM gremistas
        WHERE id = $1
        RETURNING *
    """, id)

    await conn.close()

    if gremista_deletado is None:
        raise HTTPException(
            status_code=404,
            detail="Gremista não encontrado"
        )

    return {
        "message": "GREMISTA DELETADO COM SUCESSO!",
        "gremista": dict(gremista_deletado)
    }

@app.post("/categorias")
async def criar_categoria(categorias: Categoria):
    conn = await get_db_connection()
    nova_categoria = await conn.fetchrow("""
        INSERT INTO categorias (nome_categoria)
        VALUES ($1) RETURNING *
        """,
        categorias.nome_categoria
        )
    
    await conn.close()
    return {
        "message": "CATEGORIA ADICIONADA!!",
        "categoria": dict(nova_categoria)
    }

@app.get("/categorias")
async def listar_categorias():
    conn = await get_db_connection()

    categorias = await conn.fetch("""
        SELECT * FROM categorias
        ORDER BY id
    """)

    await conn.close()

    return {
        "message": "CATEGORIAS LISTADAS COM SUCESSO!",
        "categorias": [dict(categoria) for categoria in categorias]
    }

@app.delete("/categorias/{id}")
async def deletar_categoria(id: int):
    conn = await get_db_connection()
    categoria_deletada = await conn.fetchrow("""
        DELETE FROM categorias
        WHERE id = $1
        RETURNING *
        """, id)
    
    await conn.close()

    if categoria_deletada is None:
        raise HTTPException(
            status_code=404,
            detail="Categoria não encontrada"
        )
    
    return {
        "message": "CATEGORIA DELETADA COM SUCESSO!",
        "categoria": dict(categoria_deletada)
    }

@app.post("/locais")
async def adicionar_local(locais: Local):
    conn = await get_db_connection()
    novo_local = await conn.fetchrow("""
        INSERT INTO locais (nome_local, bloco)
        VALUES ($1, $2) RETURNING *
        """,
        locais.nome_local, locais.bloco
        )
    
    await conn.close()
    return {
        "message": "LOCAL ADICIONADO!!",
        "local": dict(novo_local)
    }

@app.delete("/locais/{id}")
async def deletar_local(id: int):
    conn = await get_db_connection()
    local_deletado = await conn.fetchrow("""
        DELETE FROM locais
        WHERE id = $1
        RETURNING *
        """, id)
    
    await conn.close()

    if local_deletado is None:
        raise HTTPException(
            status_code=404,
            detail="Local não foi encontrado"
        )
    
    return {
        "message": "LOCAL DELETADO COM SUCESSO!",
        "local": dict(local_deletado)
    }

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
    return {
        "message": "ITEM CRIADO!",
        "item": dict(novo_item)
        }

@app.get("/locais")
async def listar_locais():
    conn = await get_db_connection()

    locais = await conn.fetch("""
        SELECT * FROM locais
        ORDER BY id
    """)

    await conn.close()

    return {
        "message": "LOCAIS LISTADOS COM SUCESSO!",
        "locais": [dict(local) for local in locais]
    }

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
        LEFT JOIN gremistas gr ON i.gremista_recebeu_id = gr.id
        LEFT JOIN gremistas ge ON i.gremista_entregou_id = ge.id
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
    return {
    "message": "ITENS LISTADOS COM SUCESSO!",
    "itens": list_itens
}

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

    return {
    "message": "ITEM ENCONTRADO!",
    "item": dict(item)
}


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

    return {
    "message": "ITEM ATUALIZADO COM SUCESSO!",
    "item": dict(item_atualizado)
}


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