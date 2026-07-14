# Models: Define as tabelas do BD utilizadno o SQLAlchemy, 
# espeficiando colunas, tipos, dados e relacionamentos

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base
from datetime import date

class Usuario(Base):
    __tablename__ = "usuarios"
    id: Mapped[int] = mapped_column(primary_key=True)
    # Mapped[x] indica o tipo de dados que será armazenado

    nome: Mapped[str]
    matricula: Mapped[str] = mapped_column(unique=True)
                            # Configura propriedades especiais da coluna
    cargo: Mapped[str]
    username: Mapped[str]
    email: Mapped[str]
    senha: Mapped[str]

    itens_recebidos: Mapped[list["Item"]] = relationship(back_populates="usuario_recebeu")
    # back_populates: relacionamento que existe em ambos sentidos entre as tabelas
class Categoria(Base):
    __tablename__ = "categorias"
    id: Mapped[int] = mapped_column(primary_key=True)

    nome_categoria: Mapped[str]
    itens: Mapped[list["Item"]] = relationship(back_populates="categoria")

class Local(Base):
    __tablename__ = "locais"
    id: Mapped[int] = mapped_column(primary_key=True)

    nome_local: Mapped[str]
    bloco: Mapped[str]
    itens: Mapped[list["Item"]] = relationship(back_populates="local")

class Item(Base):
    __tablename__ = "itens"

    id: Mapped[int] = mapped_column(primary_key=True)

    descricao: Mapped[str]
    data_registro: Mapped[date]
    status: Mapped[str]
    dono_recuperou: Mapped[str | None]

    categoria_id: Mapped[int] = mapped_column(ForeignKey("categorias.id"))
    local_id: Mapped[int] = mapped_column(ForeignKey("locais.id"))
    usuario_recebeu_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))

    categoria: Mapped["Categoria"] = relationship(back_populates="itens")
    local: Mapped["Local"] = relationship(back_populates="itens")
    usuario_recebeu: Mapped["Usuario"] = relationship(back_populates="itens_recebidos")