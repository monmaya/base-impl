#!/usr/bin/env bash

#
PGSVR="localhost"
PGUSR="monmaya"

if [ "$1" == "-h" -o "$1" == "-H" -o "$1" == "-help" -o "$1" == "--help" ]
then
	echo
	echo "Usage: $0 [<PG server> <PG user>]"
	echo ".   Default values: PG server: ${PGSVR} - PG user: ${PGUSR}"
	echo
	exit
fi
if [ "$1" != "" ]
then
	PGSVR="$1"
fi
if [ "$2" != "" ]
then
	PGUSR="$2"
fi

# Data product
psql -h ${PGSVR} -U ${PGUSR} -f ddl/ddl-data_product.sql
psql -h ${PGSVR} -U ${PGUSR} -c "\copy data_product(id, description, created_at_utc, updated_at_utc) from 'seeds/seed_data_product_data.csv' delimiter ',' csv header;"

#
psql -h ${PGSVR} -U ${PGUSR} -f ddl/ddl-product_port.sql
psql -h ${PGSVR} -U ${PGUSR} -c "\copy product_port(id,description, data_product_id, type, created_at_utc, updated_at_utc) from 'seeds/seed_product_port_data.csv' delimiter ',' csv header;"

# Data contract
psql -h ${PGSVR} -U ${PGUSR} -f ddl/ddl-data_contract.sql
psql -h ${PGSVR} -U ${PGUSR} -c "\copy data_contract(id,description, port_id, created_at_utc, updated_at_utc) from 'seeds/seed_data_contract_data.csv' delimiter ',' csv header;"

#
psql -h ${PGSVR} -U ${PGUSR} -c "\dt"
