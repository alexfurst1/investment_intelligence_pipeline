# Personal Investment Intelligence Pipeline with Downstream ML

# Problem Statement
 I, a 22 year old post-grad with a small amount of money, would like to learn about investing and the stock market. I would also like showcase my software, data, and machine learning engineering skills, while filling knowledge gaps through applied data and ML engineering.

# Goals: 
    - Showcase production-minded data engineering practices
    - Practice applied data engineering and improve practical ML skill
    - Design for scale, without actually scaling 
    - Extract messy financial data efficiently from multiple public sources
    - Orchestrate pipeline to run on an automatic batch schedule
    - transform and structure data in a medallion-like architecture
    - test data quality with using dbt
    - extract and engineer multiple macroeconomic signals from data
    - input cleaned data into ML model to forecast market regime
    - serve regime classification to FastAPI endpoint(s)

# Non-goals:
    - does not extract useless data
    - does not cost money to create
    - does not give recommendations
    - does not cover individual stocks, purely macroeconomic
    - does not cover day trading. 
    - does not serve to a dashboard

# Tech Stack:
    1. Ingestion
     - FRED and yfinance Python libraries

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
            -

# Trade-offs and Decisions

- **Ingestion — `fredapi` + `yfinance`.** Between them they cover every series this
  project needs, with no scraping, no API keys beyond a free FRED key, and no
  vendor cost.
- **Storage — S3-compatible object storage via LocalStack.** Bronze is Parquet in
  an S3 API-compatible bucket running locally, so the pipeline is free to run and
  reproducible on any machine. Real S3 is the deployment path — the code is
  already written against the S3 API, so moving over is a credentials and endpoint
  change, not a rewrite.
- **Query engine + warehouse — DuckDB.** Reads bronze Parquet from S3 directly, so
  there's no load stage between object storage and transforms. Columnar and
  vectorized, which suits a workload that's all full-column scans and window
  functions at single-node scale (~10⁵ rows). No server, no account — the
  warehouse is one file in the repo, so the pipeline is clone-and-run. Mature dbt
  adapter (`dbt-duckdb`).
- **Transformation — dbt Core.** Industry standard, lightweight, runs locally
  against DuckDB, and gives me lineage, `ref()`, and tests without additional
  infrastructure.
- **Testing — dbt tests in silver and gold.** Schema and data tests live next to
  the models they cover, so correctness checks run as part of `dbt build` rather
  than as a separate script.
- **Orchestration — Prefect.** A solo, mostly local project needs a lightweight
  scheduler with minimal setup. Airflow in particular — and Dagster to a lesser
  degree — carries deployment and conceptual overhead that a handful of
  dependent tasks doesn't justify.
- **ML — logistic regression, Random Forest, XGBClassifier.** Logistic regression
  as an interpretable baseline, then tree ensembles to see whether non-linear
  structure earns its complexity. Evaluated on per-class precision and recall
  rather than accuracy, since the classes are heavily imbalanced.
- **Serving — FastAPI.** Prior experience with it, and the surface area here is a
  couple of endpoints returning class probabilities from gold.
- **Infrastructure — Docker and Docker Compose.** Makes the pipeline reproducible
  across machines. Terraform is aimed at provisioning real cloud infrastructure,
  which this project doesn't have.

# Open Questions
    - should I use star schema for gold layer?
    - do I have enough data to train XGBoost and Random Forest on?
    - how far in the future should I be predicting the market regime? 1 month, quarter, year, etc... ?

# Timeline
    - 7/27 - 8/2:
      - decide ml output, complete data models, build gold and engineer features
    - 8/3 - 8/10: 
      - create gold tests, train models, tune, endpoints, orchestrate pipeline
      - plan for v2

# Success criteria
    - regimes to be classified are decided on
    - gold data model is complete
    - all gold models are built including engineered features
    - gold model tests are created
    - all 3 ML models are trained and evaluated
    - models are tuned
    - endpoints are created
    - pipeline is orchestrated
    - v2 is planned

    
