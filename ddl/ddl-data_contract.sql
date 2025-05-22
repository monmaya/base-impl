drop table if exists data_contract;

create table data_contract (
   id VARCHAR,
   description VARCHAR,
   port_id VARCHAR,
   created_at_utc TIMESTAMP,
   updated_at_utc TIMESTAMP
);

