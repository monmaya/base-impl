#!/usr/bin/env bash

# Data product
psql -h $PG_SVR -U monmaya -f ddl/ddl-data_product.sql
psql -h $PG_SVR -U monmaya -c "\copy data_product(id, description, created_at_utc, updated_at_utc) from 'seeds/seed_data_product_data.csv' delimiter ',' csv header;"

#
psql -h $PG_SVR -U monmaya -f ddl/ddl-product_port.sql
psql -h $PG_SVR -U monmaya -c "\copy product_port(id,description, data_product_id, type, created_at_utc, updated_at_utc) from 'seeds/seed_product_port_data.csv' delimiter ',' csv header;"

# Data contract
psql -h $PG_SVR -U monmaya -f ddl/ddl-data_contract.sql
psql -h $PG_SVR -U monmaya -c "\copy data_contract(id,description, port_id, created_at_utc, updated_at_utc) from 'seeds/seed_data_contract_data.csv' delimiter ',' csv header;"

