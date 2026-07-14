# Auth: Responsável pela autenticação dos usuários (administra as senhas)

from passlib.context import CryptContext #criar hash e verificar hash


pwd_context = CryptContext( #máquina de segurança
    schemes=["bcrypt"], #algoritmos
    deprecated="auto" #identifica se está ficando antigo
)

def hash_password(password: str) -> str:
    """
    Recebe uma senha em texto puro e retorna o hash dela.
    """
    return pwd_context.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    """
    Verifica se a senha digitada corresponde ao hash armazenado.
    """
    return pwd_context.verify(password, hashed_password)

