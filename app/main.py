from fastapi import FastAPI
from typing import List
from .repositories.postgresql.postgresql_repository import engine, DataProduct, DataContract, DataProductContract, DataContractSubscription
from sqlmodel import select, Session

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to Data Product API"}


@app.get("/data-products/")
def list_data_products() -> List[DataProduct]:
    with Session(engine) as session:
        statement = select(DataProduct)
        return session.exec(statement).all()


@app.post("/data-products/")
def create_data_product(product: DataProduct) -> DataProduct:
    with Session(engine) as session:
        session.add(product)
        session.commit()
        session.refresh(product)
        return product


@app.post("/data-product-contract/")
def link_contract_to_product(product_contract: DataProductContract) -> DataProductContract:
    with Session(engine) as session:
        session.add(product_contract)
        session.commit()
        session.refresh(product_contract)
        return product_contract


@app.get("/data-contracts/")
def list_data_contracts() -> List[DataContract]:
    with Session(engine) as session:
        statement = select(DataContract)
        return session.exec(statement).all()


@app.get("/data-contracts/{id}/subscriptions/")
def get_data_contract_subscriptions(id) -> List[DataContractSubscription]:
    with Session(engine) as session:
        contract = session.exec(select(DataContract).where(DataContract.id==id)).one()
        return contract.subscriptions
