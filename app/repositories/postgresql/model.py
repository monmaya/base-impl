from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime


class DataProduct(SQLModel, table=True):
    __tablename__ = "data_product"

    id: str = Field(primary_key=True)
    name: str
    description: str
    owner: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    data_contracts: list["DataProductContract"] = Relationship(back_populates="data_product")


    def get_input_contracts(self):
        input_contracts = []
        for contract in self.data_contracts:
            if contract.relation_type=="input":
                input_contracts.append(contract)
        return input_contracts


    def get_output_contracts(self):
        output_contracts = []
        for contract in self.data_contracts:
            if contract.relation_type=="output":
                output_contracts.append(contract)
        return output_contracts


class DataContract(SQLModel, table=True):
    __tablename__ = "data_contract"

    id: str = Field(primary_key=True)
    data_products: list["DataProductContract"] = Relationship(back_populates="data_contract")
    subscriptions: list["DataContractSubscription"] = Relationship(back_populates="data_contract")


class DataProductContract(SQLModel, table=True):
    __tablename__ = "data_product_contract"
    data_product_id: str = Field(foreign_key="data_product.id", primary_key=True)
    data_product: Optional["DataProduct"] = Relationship(back_populates="data_contracts")
    data_contract_id: str = Field(foreign_key="data_contract.id", primary_key=True)
    data_contract: Optional["DataContract"] = Relationship(back_populates="data_products")
    relation_type: str


class DataContractSubscription(SQLModel, table=True):
    __tablename__ = "data_contract_subscription"
    user_id: str = Field(primary_key=True)
    data_contract_id: str = Field(foreign_key="data_contract.id", primary_key=True)
    data_contract: Optional["DataContract"] = Relationship(back_populates="subscriptions")
    start_date: datetime = Field(default_factory=datetime.utcnow)
    end_date: Optional[datetime]
