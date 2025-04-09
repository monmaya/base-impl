from fastapi import FastAPI, HTTPException
from fastapi.openapi.utils import get_openapi
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI()

# In-memory database (replace with real database in production)
data_products_db = []
data_contracts_db = []

class DataProduct(BaseModel):
    id: str
    name: str
    description: str
    owner: str
    created_at: datetime
    updated_at: datetime

class DataContract(BaseModel):
    id: str
    data_product_id: str
    terms: str
    validity_period: dict

@app.get("/")
def read_root():
    return {"message": "Welcome to Data Referential Management API"}

@app.get("/data-products")
def list_data_products() -> List[DataProduct]:
    return data_products_db

@app.post("/data-products")
def create_data_product(product: DataProduct) -> DataProduct:
    data_products_db.append(product)
    return product

@app.get("/data-products/{product_id}")
def get_data_product(product_id: str) -> DataProduct:
    for product in data_products_db:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Data product not found")

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
