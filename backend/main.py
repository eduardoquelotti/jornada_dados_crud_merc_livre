from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine
import models
from router import router

# Criar as tabelas no banco de dados (idealmente isso seria feito em um script separado)
models.Base.metadata.create_all(bind=engine)

# Instância da aplicação FastAPI com metadados adicionais
app = FastAPI(
    title="Gestão de Estoque - Mercado Livre",
    description="API para gerenciamento de estoque, produtos e categorias do Mercado Livre",
    version="1.0.0"
)

# Incluir o roteador principal
app.include_router(router)

# Ponto de entrada da aplicação
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)