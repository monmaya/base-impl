drop table if exists data_product;

create table data_product (
    id VARCHAR,
    description VARCHAR,
    contract_id VARCHAR,
    created_at_utc TIMESTAMP,
    updated_at_utc TIMESTAMP
);

