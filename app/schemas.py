# Schemas: Define os BASEMODEL utiliazdos para validar dados que entram e saem da API

from datetime import date
from pydantic import BaseModel

class UsuarioCreate(BaseModel):
    nome: str
    matricula: str
    cargo: str
    username: str
    email: str
    senha: str
# Validação dos dados de cadastro de usuário

class UsuarioLogin(BaseModel):
    username: str
    senha: str
# Validação de dados do login

class UsuarioResponse(BaseModel):
    id: int
    nome: str
    matricula: str
    cargo: str
    username: str
    email: str
# Modelo de informações retornadas
    class Config:
        from_attributes = True

class CategoriaCreate(BaseModel):
    nome_categoria: str

class CategoriaResponse(BaseModel):
    id: int
    nome_categoria: str
    class Config:
        from_attributes = True

class LocalCreate(BaseModel):
    nome_local: str
    bloco: str

class ItemCreate(BaseModel):
    descricao: str
    data_registro: date
    status: str
    dono_recuperou: str | None = None
    categoria_id: int
    local_id: int
    usuario_recebeu_id: int