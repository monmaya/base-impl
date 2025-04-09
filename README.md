# base-impl
Base implementation for the data-related referential management service:
https://github.com/monmaya/specifications

# API Service

This project provides a RESTful API service with OpenAPI documentation.

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Run the server: `uvicorn main:app --reload --port 8020`

## Features
- Automatic OpenAPI documentation at `/docs`
- Custom OpenAPI schema generation
- Sample root endpoint

## Accessing OpenAPI
- Interactive docs: http://localhost:8020/docs
- OpenAPI JSON: http://localhost:8020/openapi.json

