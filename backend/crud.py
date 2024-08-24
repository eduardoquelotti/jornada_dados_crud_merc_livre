from sqlalchemy.orm import Session
from schemas import ProductUpdate, ProductCreate
from models import ProductModel
from sqlalchemy.exc import SQLAlchemyError


def get_product(db: Session, product_id: int):
    """
    Retorna um produto específico pelo ID.
    
    :param db: Sessão do banco de dados.
    :param product_id: ID do produto.
    :return: Produto correspondente ou None se não for encontrado.
    """
    return db.query(ProductModel).filter(ProductModel.id == product_id).first()


def get_products(db: Session):
    """
    Retorna todos os produtos cadastrados.
    
    :param db: Sessão do banco de dados.
    :return: Lista de todos os produtos.
    """
    return db.query(ProductModel).all()


def create_product(db: Session, product: ProductCreate):
    """
    Cria um novo produto no banco de dados.
    
    :param db: Sessão do banco de dados.
    :param product: Dados do produto a ser criado.
    :return: Produto criado.
    """
    try:
        db_product = ProductModel(**product.model_dump())
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return db_product
    except SQLAlchemyError as e:
        db.rollback()
        raise e


def delete_product(db: Session, product_id: int):
    """
    Deleta um produto específico pelo ID.
    
    :param db: Sessão do banco de dados.
    :param product_id: ID do produto a ser deletado.
    :return: Produto deletado ou None se não for encontrado.
    """
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()

    if db_product is None:
        return None

    try:
        db.delete(db_product)
        db.commit()
        return db_product
    except SQLAlchemyError as e:
        db.rollback()
        raise e


def update_product(db: Session, product_id: int, product: ProductUpdate):
    """
    Atualiza um produto específico pelo ID.
    
    :param db: Sessão do banco de dados.
    :param product_id: ID do produto a ser atualizado.
    :param product: Dados atualizados do produto.
    :return: Produto atualizado ou None se não for encontrado.
    """
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()

    if db_product is None:
        return None

    if product.name is not None:
        db_product.name = product.name
    if product.description is not None:
        db_product.description = product.description
    if product.price is not None:
        db_product.price = product.price
    if product.categoria is not None:
        db_product.categoria = product.categoria
    if product.email_fornecedor is not None:
        db_product.email_fornecedor = product.email_fornecedor

    try:
        db.commit()
        db.refresh(db_product)
        return db_product
    except SQLAlchemyError as e:
        db.rollback()
        raise e