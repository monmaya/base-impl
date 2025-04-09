Data-related referential management service - Base implementation
=================================================================

# Table of Content (ToC)
* [Overview](#overview)
* [References](#references)
  * [Data products](#data-products)
  * [Data contracts](#data-contracts)

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

# Getting started
This project provides a RESTful API service with OpenAPI documentation.

## Features
- Automatic OpenAPI documentation at `/docs`
- Custom OpenAPI schema generation
- Sample root endpoint

## Accessing OpenAPI
- Interactive docs: http://localhost:8020/docs
- OpenAPI JSON: http://localhost:8020/openapi.json

# Installation
1. Install dependencies: `pip install -r requirements.txt`
2. Run the server: `uvicorn main:app --reload --port 8020`
