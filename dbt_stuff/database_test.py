import duckdb

con = duckdb.connect('investment_intel.duckdb')

con.sql("INSTALL httpfs; LOAD httpfs;")
con.sql("""
    SET s3_endpoint='localhost:4566';
    SET s3_access_key_id='test';
    SET s3_secret_access_key='test';
    SET s3_use_ssl=false;
    SET s3_url_style='path';
""")

con.sql("SELECT * FROM stg_fred_dgs10 LIMIT 5").show()
