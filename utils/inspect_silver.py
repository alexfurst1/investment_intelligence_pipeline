import duckdb

con = duckdb.connect('dbt_stuff/investment_intel.duckdb')
con.sql('SELECT * FROM signals_joined LIMIT 1').show()