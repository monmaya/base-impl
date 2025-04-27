# Relational Model

<br/><br/><br/><br/>

```mermaid

erDiagram

    DATA_PRODUCT {
        uuid id PK "Data product unique identifier"
        string description "Description of the data product"
        uuid contact_id FK "Ref: CONTACT"
        timestamp created_at_utc "Creation date"
        timestamp updatd_at_utc "Last modification date"
    }

    PORT {
        uuid id PK "Port unique identifier"
        uuid data_product_id FK "Ref: DATA_PRODUCT"
        enum type "['input', 'output']"
        
    }

    DATA_CONTRACT {
        string id PK "Data Contract unique identifier"
        timestamp created_at_utc "Creation date"
        timestamp updatd_at_utc "Last modification date"
    }

    DATA_CONTRACT_VERSION {
        string data_contract_id PK, FK "Ref: DATA_CONTRACT"
        string version_number PK "Based on semantic versioning"
    }

    DATA_CONTRACT_INSTANCE {
        uuid contract_instance_id PK
        string version_number UK, FK "Ref: DATA_CONTRACT_VERSION"
        string ref_standard UK "Data Contract standard (dcs, odcs, etc.)"
        uuid schema_id FK Not null, "Ref: CONTRACT_SCHEMA"
    }
    
    DATA_CONTRACT_SUBSCRIPTION {
        uuid data_contract_id PK, FK "Ref: DATA_CONTRACT"
        uuid contact_id PK, FK "Ref: CONTACT"
        timestamp start_time_utc "Subscription start date"
        timestamp end_time_utc "Subscription start date"
    }

    CONTACT {
        uuid id PK "User unique identifier"
        string email "User email"
        string team
    }

    CONTRACT_SCHEMA {
        uuid id PK    
        string schema_uri "Link to the schema document"
        timestamp created_at_utc "Creation date"
        timestamp updatd_at_utc "Last modification date"
    }
    CONTRACT_QUALITY {
        uuid id PK    
        string quality_uri "Link to the quality document"
        timestamp created_at_utc "Creation date"
        timestamp updatd_at_utc "Last modification date"
    }
    CONTRACT_SPECIFICATION {
        uuid id PK    
        string schema_uri "Link to the specification document"
        timestamp created_at_utc "Creation date"
        timestamp updatd_at_utc "Last modification date"
    }
    CONTRACT_SLO {
        uuid id PK    
        string schema_uri "Link to the slo document"
        timestamp created_at_utc "Creation date"
        timestamp updatd_at_utc "Last modification date"
    }


    DATA_PRODUCT ||--o{ PORT : "Product delivered in n ports"
    DATA_PRODUCT ||--o{ CONTACT : "Product Owner"
    PORT ||--o{ DATA_CONTRACT : "Composed of n data contracts"
    DATA_CONTRACT ||--o{ DATA_CONTRACT_VERSION : "Contract versions"
    DATA_CONTRACT_VERSION ||--o{ DATA_CONTRACT_INSTANCE : "Contract instances"
    DATA_CONTRACT ||--o{ DATA_CONTRACT_SUBSCRIPTION : ""
    CONTACT ||--o{ DATA_CONTRACT_SUBSCRIPTION : "Notified on contract changes (example: data consumer)"

    DATA_CONTRACT_INSTANCE ||--o{ CONTRACT_SCHEMA : "Contract instances"
    DATA_CONTRACT_INSTANCE ||--o{ CONTRACT_QUALITY : "Contract instances"
    DATA_CONTRACT_INSTANCE ||--o{ CONTRACT_SPECIFICATION : "Contract instances"
    DATA_CONTRACT_INSTANCE ||--o{ CONTRACT_SLO : "Contract instances"


  ```

