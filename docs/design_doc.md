# Personal Investment Intelligence Pipeline with Downstream ML

# Problem Statement
 I, a 22 year old post-grad with a small amount of money, would like to learn about investing long term, medium term, and short term. I would also like showcase my software, data, and machine learning engineering skills, while filling knowledge gaps through applied data and ML engineering.

# Goals: 
    - Showcase production-minded data engineering practices
    - Practice applied data engineering and improve practical ML skill
    - Design for scale, without actually scaling 
    - Extract messy financial data efficiently from multiple public sources
    - Orchestrate pipeline to run on an automatic batch schedule
    - transform and structure data in a medallion-like architecture
    - test data quality with using dbt
    - extract and engineer multiple macroeconomic signals from data
    - input cleaned data into ML model to recommend asset allocation with horizon variable
    - serve recommendations with FastAPI endpoint(s)

# Non-goals:
    - does not extract useless data
    - does not cost more than $20
    - is not intended for multiple users, built for a single user at a time
    - not a live trading system, no money is being transferred, purely recommendations
    - does not cover individual stocks, purely macroeconomic
    - recommendations are historically grounded but not guaranteed.
    - does not cover day trading. Investment recommendations are for 1 yr - 30 yr horizons.

# Tech Stack:
    1. Ingestion
     - FREDAPI python library, requests for Yahoo Finance

    2. Storage
     - LocalStack offline S3 bucket to mimic AWS free tier for bronze layer

    3. Query Engine
     - DuckDB for querying bronze Parquet files
    
    4. Orchestration
     - Prefect locally with decorators for v1, stand up server with UI and scheduling for v2.

    5. Transformation
     - dbt Core for silver and gold, along with testing

    6. Warehouse
     - DuckDB database for silver and gold layers

    7. ML
     - XGBoost & Random Forest, Linear Reg. for baseline

    8. Testing
     - python assertions in bronze, dbt in silver and gold
     - dbt tracks data lineage as well

    9. Serving
     - FastAPI endpoint

    10. Infrastructure
     - Docker for containerization, Docker Compose for spin up and runtime

# Data Model
    1. To be fetched from FRED:
        - DGS10 (yield curve slope)
        - DGS2 
        - CPIAUCSL (inflation)
        - FEDFUNDS (fed rate)
        - UNRATE (unemployment rate)
        - GDP (gdp growth, useful for regime detection)
        - DGS30 (good for broader yield picture)
    2. To be fetched from Yahoo Finance:
        - asset signals (sharpe ratio, max drawdown, volatility regime)

    Schemas:
        Bronze layer:
            - raw parquet files, 
        Silver layer:
            - 
        Gold layer:
            - ML model predictions

# Trade-offs and Decisions
    - Ingestion: FRED and Yahoo Finance libraries contain every piece of data I need.
    - Storage: AWS free tier, I won't need to go above free limits, gives me exposure to AWS services
    - Query engine: spark is overkill, regular pandas querying loads into memory which we don't want, and duckDB runs on Parquet files, and does not load queries or data into memory. My dataset won't be too big, but I want to use industry standard techniques as well, so DuckDB is the best choice.
    - Orchestration: Prefect because this is a solo, mostly local project, that requires a lightweight architecture and flexibility. Dagster and Airflow especially are too overkill.
    - Transformation: dbt. Industry standard, lightweight, works well locally, moderate learning curve.
    - Warehouse: DuckDB for silver and gold warehouse layers. Was originally going to use regular PostgreSQL, but DuckDB is columnar, and I'm already using it for my query engine.
    - ML: 
    - Testing: Since dbt is industry standard, I will use it for schema enforcement in the silver layer. In bronze, and maybe even gold, python assertations will do.
    - Serving: I have prior experience with FastAPI, so I will use it for simple endpoints
    - Infra: Docker Compose. Terraform is overkill, and this will make my pipeline recreatable across different machines.

# Open Questions
    - should I use star schema for gold layer?
    - do I have enough data to train XGBoost and Random Forest on?
    - 

# Timeline

# Success criteria
    - docker is set up
    - all needed data can be pulled from fredapi
    - all medallion layers are set up
    - pipeline can run from each stage to the next
    - all pipeline layers are complete
    - data testing exists
    - ML is trained and can conduct inference
    - 

    
