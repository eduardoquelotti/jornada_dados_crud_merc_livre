from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from schemas import ProductResponse, ProductUpdate, ProductCreate
from typing import List
from crud import (
    create_product,
    get_products,
    get_product,
    delete_product,
    update_product
)

router = APIRouter()

# Criar rota para buscar todos os itens
@router.get("/products", response_model=List[ProductResponse])
def read_all_products(db: Session = Depends(get_db)):
    products = get_products(db)
    return products

# Criar rota para buscar item
@router.get("/products/{product_id}", response_model=ProductResponse)
def read_one_product(product_id: int, db: Session = Depends(get_db)):
    product_db = get_product(db=db, product_id=product_id)
    if product_db is None:
        raise HTTPException(status_code=404, detail="Você está querendo buscar um id inexistente")
    return product_db

# Criar rota para adicionar um item
@router.post("/products", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(product=product, db=db)

# Criar rota para deletar um item
@router.delete("/products/{product_id}", response_model=ProductResponse)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product_db = delete_product(product_id=product_id, db=db)
    if product_db is None:
        raise HTTPException(status_code=404, detail="Você está querendo deletar um id inexistente")
    return product_db

# Criar rota para atualizar um item
@router.put("/products/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    product_db = update_product(product_id=product_id, db=db, product=product)
    if product_db is None:
        raise HTTPException(status_code=404, detail="Você está querendo atualizar um id inexistente")
    return product_db