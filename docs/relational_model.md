# Relational Model

<br/><br/><br/><br/>

```mermaid

erDiagram

    DATA_PRODUCT {
        string id PK
        string description
        string owner
        date created_at
        date updatd_at
    }

    DATA_CONTRACT {
        string id PK
    }

    DATA_PRODUCT }o--o{ DATA_PRODUCT_CONTRACT : ""

    DATA_PRODUCT_CONTRACT {
        string data_product_id PK "FK -> DATA_PRODUCT"
        string data_contract_id PK "FK -> DATA_CONTRACT"
        enum relation_type "['input, 'output']"
    }

    DATA_CONTRACT_SUBSCRIPTION {
        string fed_id PK "FEDID of the subscribed collaborator"
        string data_contract_id PK "FK -> DATA_CONTRACT"
        date start_date
        date end_date 
    }

    DATA_CONTRACT ||--o{ DATA_PRODUCT_CONTRACT : ""

    DATA_CONTRACT_SUBSCRIPTION ||--|| DATA_CONTRACT : ""


  ```

