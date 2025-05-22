Data-related referential management service - Base implementation
=================================================================

# Table of Content (ToC)

# Overview
[This project](https://github.com/monmaya/base-impl) is a reference implementation
for MonMaya: https://github.com/monmaya/specifications

MonMaya is a collection of services to manage a referential for data-related
objects, like for instance data products, data contracts, data quality specifications,
data quality reports, data metrics, Service Level Objectives (SLO) and, more generally,
any type or concept appearing at a high level in data contracts.

Even though the members of the GitHub organization may be employed by some companies,
they speak on their personal behalf and do not represent these companies.

# References

## MonMaya
* Specifications: https://github.com/monmaya/specifications

## Data products
* Linux Foundation's Open Data Product Specification (ODPS): https://opendataproducts.org/
* Innoq's specification for Data Products: https://dataproduct-specification.com/
* Open Data Mesh (ODM)'s Data Product Descriptor Specification (DPDS): https://github.com/opendatamesh-initiative/odm-specification-dpdescriptor

## Data contracts
* Open Data Contract Specification (ODCS)
  * Reader-friendly, dedicated site: https://bitol-io.github.io/open-data-contract-standard/latest/
  * GitHub home page: https://github.com/bitol-io/open-data-contract-standard
* Innoq's Data Contract specification: https://datacontract.com/
* [Andrew Jones' Git repository supporting his book about data contracts](https://github.com/PacktPublishing/Driving-Data-Quality-with-Data-Contracts)
  * [Andrew Jones' Git repository supporting his book about data contracts - Chapter 08: samples of contracts for customer profiles](https://github.com/PacktPublishing/Driving-Data-Quality-with-Data-Contracts/tree/main/Chapter08/contracts)
  * [Andrew Jones' Git repository supporting his book about data contracts - Chapter 03: samples of contracts for order events](https://github.com/PacktPublishing/Driving-Data-Quality-with-Data-Contracts/blob/main/Chapter03/order_events.yaml)

# Getting started
This project provides a RESTful API service with OpenAPI documentation.

## Features
- Automatic OpenAPI documentation at `/docs`
- Custom OpenAPI schema generation
- Sample root endpoint

## Accessing OpenAPI
- Interactive docs: http://localhost:8020/docs
- OpenAPI JSON: http://localhost:8020/openapi.json

## Database management

### Explore the content of the database
* Browse all the records:
```bash
psql -h $PG_SVR -U monmaya -f db-explore/explore-all-in-one.sql
```

### Bootstrap the database
* Bootstrap the database:
```bash
./db-loader/loader-pg.sh
```

# Installation
1. Install dependencies: `pip install -r requirements.txt`
2. Run the server: `uvicorn main:app --reload --port 8020`

## PostgreSQL

### Quick setup for the use cases
* Specify a few environment variables
  + For local PostgreSQL server on MacOS:
```bash
$ PG_SVR="localhost"; PG_ADM_USR="$USER"
```
  + For local PostgreSQL server on Linux:
```bash
$ PG_SVR="localhost"; PG_ADM_USR="postgres"
```
  + For AWS RDS PostgreSQL service (set the proxy endpoint to
    the AWS RDS proxy one):
```bash
$ PG_SVR="project-proxy.proxy-someid.us-east-1.rds.amazonaws.com"; PG_ADM_USR="postgres"
```

### Create a database and associated user

#### Monmaya database and user
* Create on PostgreSQL a `monmaya` database and a `monmaya` user:
```bash
$ psql -h $PG_SVR -U $PG_ADM_USR -d postgres -c "create database monmaya;"
CREATE DATABASE
$ psql -h $PG_SVR -U $PG_ADM_USR -d postgres -c "create user monmaya with encrypted password '<monmaya-pass>'; grant all privileges on database monmaya to monmaya;"
CREATE ROLE
GRANT
$ psql -h $PG_SVR -U $PG_ADM_USR -d monmaya -c "grant all on schema public to monmaya;"
GRANT
```

* Check that the access to the PostgreSQL database works:
```bash
$ psql -h $PG_SVR -U monmaya -c "select 42 as nb;"
 nb 
----
 42
(1 row)
```

### Import files, create and browse tables
* List the tables:
```bash
$ psql -h $PG_SVR -U monmaya -c "\dt"
```

* Describe a given table:
```bash
$ psql -h $PG_SVR -U monmaya -c "\d mytable"
```

* Execute a specific SQL script:
```bash
$ psql -h $PG_SVR -U monmaya -f ddl/ddl-data_product.sql
```

* Load CSV data into a table
  * Download the country information CSV data file from
    [Geonames](https://download.geonames.org/export/dump/):
```bash
$ curl https://download.geonames.org/export/dump/countryInfo.txt -o db/duckdb/data/csv/countryInfo.txt
```
  * Remove the header comments:
```bash
$ tail -n +51 db/duckdb/data/csv/countryInfo.txt > db/duckdb/data/csv/countryInfo.csv
```
  * Parse and load the data into PostgreSQL
    (`<CTRL-V-TAB>` means: on the terminal, press successively the Control-V
	  and the TAB keys):
```bash
$ psql -h $PG_SVR -U monmaya -c "\copy data_product(id, description, contract_id, created_at_utc, updated_at_utc) from 'seeds/seed_data_product_data.csv delimiter ',' csv header;"
```
  
* Display the content of a table:
```bash
$ psql -h $PG_SVR -U monmaya -c "select iso_alpha2, iso_alpha3, name, capital, continent, currency_code, languages from country_info;"
```



