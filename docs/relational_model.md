# Relational Model

<br/><br/><br/><br/>

```mermaid

erDiagram

    DATA_PRODUCT {
        uuid id PK "Data product nique identifier"
        string description "Description of the data product"
        uuid owner_id "FK -> USER"
        date created_at_utc "Creation date"
        date updatd_at_utc "Last modification date"
    }

    PORT {
        uuid id PK "Port unique identifier"
        string name "Port name"
        uuid data_product_id "FK -> DATA_PRODUCT"
    }

    DATA_CONTRACT {
        uuid id PK "Data contract unique identifier"
    }

    DATA_CONTRACT_VERSION {
        string version_number PK "Based on semantic versioning"
        uuid data_contract_id PK "FK -> DATA_CONTRACT"
        string contract_uri "Link to this data contract version"
    }

    
    DATA_CONTRACT_SUBSCRIPTION {
        uuid user_id PK "FK -> DATA_CONTRACT"
        uuid data_contract_id PK "FK -> DATA_CONTRACT"
        date start_date_utc "Subscription start date"
        date end_date_utc "Subscription start date"
    }

    DATA_PRODUCT ||--o{ PORT : "Product delivered in n ports"
    PORT ||--o{ DATA_CONTRACT : "Composed of n Data Contracts"
    DATA_CONTRACT ||--o{ DATA_CONTRACT_VERSION : "Contract versions"
    DATA_CONTRACT ||--o{ DATA_CONTRACT_SUBSCRIPTION : "Subscribed to data contract changes"


  ```

