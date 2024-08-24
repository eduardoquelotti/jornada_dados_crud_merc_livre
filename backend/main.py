# jornada_dados_crud_mercado_livre/backend/main.py

from fastapi import FastAPI
from database import engine
import models
from router import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)
