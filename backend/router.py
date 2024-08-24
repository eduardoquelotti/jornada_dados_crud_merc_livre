from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from schemas import ProductResponse, ProductUpdate, ProductCreate
from typing import List
from crud import (
    create_product,
    get_products,
    get_product,
    delete_product,
    update_product,
)
import logging

router = APIRouter()

# Configuração básica de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@router.post("/products/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product_route(product: ProductCreate, db: Session = Depends(get_db)):
    logger.info("Criando um novo produto")
    return create_product(db=db, product=product)


@router.get("/products/", response_model=List[ProductResponse])
def read_all_products_route(db: Session = Depends(get_db)):
    products = get_products(db)
    if not products:
        logger.warning("Nenhum produto encontrado")
    return products


@router.get("/products/{product_id}", response_model=ProductResponse)
def read_product_route(product_id: int, db: Session = Depends(get_db)):
    db_product = get_product(db, product_id=product_id)
    if db_product is None:
        logger.error(f"Produto com ID {product_id} não encontrado")
        raise HTTPException(status_code=404, detail="Produto não encontrado. Verifique o ID e tente novamente.")
    return db_product


@router.delete("/products/{product_id}", response_model=ProductResponse)
def delete_product_route(product_id: int, db: Session = Depends(get_db)):
    db_product = delete_product(db, product_id=product_id)
    if db_product is None:
        logger.error(f"Falha ao deletar: Produto com ID {product_id} não encontrado")
        raise HTTPException(status_code=404, detail="Produto não encontrado para exclusão. Verifique o ID e tente novamente.")
    logger.info(f"Produto com ID {product_id} foi deletado com sucesso")
    return db_product


@router.put("/products/{product_id}", response_model=ProductResponse)
def update_product_route(
    product_id: int, product: ProductUpdate, db: Session = Depends(get_db)
):
    db_product = update_product(db, product_id=product_id, product=product)
    if db_product is None:
        logger.error(f"Falha ao atualizar: Produto com ID {product_id} não encontrado")
        raise HTTPException(status_code=404, detail="Produto não encontrado para atualização. Verifique o ID e tente novamente.")
    logger.info(f"Produto com ID {product_id} foi atualizado com sucesso")
    return db_product