# Relational Model

<br/><br/><br/><br/>

```mermaid

erDiagram

    DATA_PRODUCT {
        uuid id PK "Data product unique identifier"
        string description "Description of the data product"
        uuid owner_id FK "Ref: USER"
        date created_at_utc "Creation date"
        date updatd_at_utc "Last modification date"
    }

    PORT {
        uuid id PK "Port unique identifier"
        string name "Port name"
        uuid data_product_id FK "Ref: DATA_PRODUCT"
    }

    DATA_CONTRACT {
        string id PK "Contract identifier (unique composed with version_number)"
        string version_number PK "Based on semantic versioning"
        date created_at_utc "Contract version creation date"
    }

    DATA_CONTRACT_INSTANCE {
        uuid data_contract_id PK "FK -> DATA_CONTRACT"
        string version_number PK "FK -> DATA_CONTRACT"
        string ref_standard "Data Contract standard (dcs, odcs, etc.)"
        string contract_uri "Link to this data contract instance"
    }
    
    DATA_CONTRACT_SUBSCRIPTION {
        uuid user_id PK "FK -> DATA_CONTRACT"
        uuid data_contract_id PK "FK -> DATA_CONTRACT"
        date start_date_utc "Subscription start date"
        date end_date_utc "Subscription start date"
    }


    DATA_PRODUCT ||--o{ PORT : "Product delivered in n ports"
    PORT ||--o{ DATA_CONTRACT : "Composed of n data contracts"
    DATA_CONTRACT ||--o{ DATA_CONTRACT_INSTANCE : "Contract instances"
    DATA_CONTRACT ||--o{ DATA_CONTRACT_SUBSCRIPTION : "Notified on contract changes"


  ```

