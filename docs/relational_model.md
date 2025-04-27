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
        string name "Port name"
        uuid data_product_id FK "Ref: DATA_PRODUCT"
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
        uuid instance_id PK "Instance unique identifier"
        string version_number FK "Ref: DATA_CONTRACT_VERSION"
        string ref_standard "Data Contract standard (dcs, odcs, etc.)"
        string contract_uri "Link to this data contract instance"
        timestamp created_at_utc "Creation date"
        timestamp updatd_at_utc "Last modification date"
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


    DATA_PRODUCT ||--o{ PORT : "Product delivered in n ports"
    DATA_PRODUCT ||--o{ CONTACT : "Product Owner"
    PORT ||--o{ DATA_CONTRACT : "Composed of n data contracts"
    DATA_CONTRACT ||--o{ DATA_CONTRACT_VERSION : "Contract versions"
    DATA_CONTRACT_VERSION ||--o{ DATA_CONTRACT_INSTANCE : "Contract instances"
    DATA_CONTRACT ||--o{ DATA_CONTRACT_SUBSCRIPTION : ""
    CONTACT ||--o{ DATA_CONTRACT_SUBSCRIPTION : "Notified on contract changes (example: data consumer)"

    EVENT_LOG {
        uuid id PK "Event unique identifier"
        enum event_type "'subscribe', 'publish', etc."
        string data_contract_id FK "Ref: DATA_CONTRACT"
        uuid contact_id FK "Ref: CONTACT"
        timestamp event_time_utc "Event time"
        json details "Event details"
    }

  ```

