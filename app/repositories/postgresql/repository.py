from sqlmodel import create_engine
from typing import List
from .model import DataProduct, DataContract, DataProductContract, DataContractSubscription
from sqlmodel import SQLModel
from sqlmodel import select, Session


class Repository():
    def __init__(self, db_url):
        self.db_url = db_url
        self.engine = create_engine(self.db_url)
        SQLModel.metadata.create_all(self.engine)        


    def get_data_products(self):
        with Session(self.engine) as session:
            statement = select(DataProduct)
            return session.exec(statement).all()


    def create_data_product(self, product: DataProduct) -> DataProduct:
        with Session(self.engine) as session:
            session.add(product)
            session.commit()
            session.refresh(product)
            return product


    def link_contract_to_product(self, product_contract: DataProductContract) -> DataProductContract:
        with Session(self.engine) as session:
            session.add(product_contract)
            session.commit()
            session.refresh(product_contract)
            return product_contract


    def get_contract_subscriptions(self, contract_id) -> List[DataContractSubscription]:
        with Session(self.engine) as session:
            contract = session.exec(select(DataContract).where(DataContract.id==contract_id)).one()
            print(contract)
            return contract.subscriptions


    def get_data_contracts(self) -> List[DataContract]:
        with Session(self.engine) as session:
            statement = select(DataContract)
            return session.exec(statement).all()


    def subscribe(self, contract_id, fed_id):
        with Session(self.engine) as session:
            contract = session.exec(select(DataContract).where(DataContract.id==contract_id)).one()
            subscription = DataContractSubscription(
                data_contract=contract,
                fed_id=fed_id
            )
            session.add(subscription)
            session.commit()
            session.refresh(subscription)
            return subscription

