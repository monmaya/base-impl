from fastapi import FastAPI, HTTPException, Depends
from fastapi.openapi.utils import get_openapi
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from sqlalchemy import create_engine, Column, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import os

# Database setup
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/data_referential")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Database models
class DBDataProduct(Base):
    __tablename__ = "data_products"
    
    id = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)
    owner = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

class DBDataContract(Base):
    __tablename__ = "data_contracts"
    
    id = Column(String, primary_key=True, index=True)
    data_product_id = Column(String, index=True)
    terms = Column(Text)
    validity_period_start = Column(DateTime)
    validity_period_end = Column(DateTime)

# Create tables
Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

# Pydantic models
class DataProduct(BaseModel):
    id: str
    name: str
    description: str
    owner: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True

class DataContract(BaseModel):
    id: str
    data_product_id: str
    terms: str
    validity_period: dict
    
    class Config:
        orm_mode = True

@app.get("/")
def read_root():
    return {"message": "Welcome to Data Referential Management API"}

@app.get("/data-products")
def list_data_products(db: Session = Depends(get_db)) -> List[DataProduct]:
    db_products = db.query(DBDataProduct).all()
    return db_products

@app.post("/data-products")
def create_data_product(product: DataProduct, db: Session = Depends(get_db)) -> DataProduct:
    db_product = DBDataProduct(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@app.get("/data-products/{product_id}")
def get_data_product(product_id: str, db: Session = Depends(get_db)) -> DataProduct:
    db_product = db.query(DBDataProduct).filter(DBDataProduct.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Data product not found")
    return db_product

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Data Referential Management API",
        version="1.0.0",
        description="API for managing data-related objects",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
