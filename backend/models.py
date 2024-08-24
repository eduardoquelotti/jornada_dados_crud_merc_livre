from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from database import Base

class ProductModel(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    description = Column(String(500), index=True)
    price = Column(Float, nullable=False, index=True)
    categoria = Column(String(100), nullable=False, index=True)
    email_fornecedor = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime(timezone=True), default=func.now(), index=True)
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now(), index=True)