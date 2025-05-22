drop table if exists product_port;

create table product_port (
  id VARCHAR,
  description VARCHAR,
  data_product_id VARCHAR,
  type VARCHAR,
  created_at_utc TIMESTAMP,
  updated_at_utc TIMESTAMP
);

