import os
from fastapi import FastAPI
from typing import List
from .repositories.postgresql.model import DataProduct, DataContract, DataProductContract, DataContractSubscription
from .repositories.postgresql.repository import Repository as PostgresqlRepository


app = FastAPI()


postgresql_repository = PostgresqlRepository(
    db_url=os.getenv("DATABASE_URL")
)


@app.get("/")
def read_root():
    return {"message": "Welcome to Data Product API"}


@app.get("/data-products/")
def list_data_products() -> List[DataProduct]:
    return postgresql_repository.get_data_products()


@app.post("/data-products/")
def create_data_product(product: DataProduct) -> DataProduct:
    return postgresql_repository.create_data_product(product)


@app.post("/data-product-contract/")
def link_contract_to_product(product_contract: DataProductContract) -> DataProductContract:
    return postgresql_repository.link_contract_to_product(product_contract)


@app.get("/data-contracts/")
def list_data_contracts() -> List[DataContract]:
    return postgresql_repository.get_data_contracts()


@app.get("/data-contracts/{id}/subscriptions/")
def get_data_contract_subscriptions(id) -> List[DataContractSubscription]:
    return postgresql_repository.get_contract_subscriptions(contract_id=id)


@app.put("/data-contracts/{id}/subscribe/")
def subscribe_to_data_contract(id, fed_id):
    return postgresql_repository.subscribe(contract_id=id, fed_id=fed_id)

