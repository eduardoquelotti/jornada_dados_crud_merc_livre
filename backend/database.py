from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Declarar URL do banco
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgres/mydatabase"

# Criar a engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Criar a sessão do banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Criar a Base do ORM
Base = declarative_base()

# Declarar função para gerar sessões (substitui o uso do with)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close