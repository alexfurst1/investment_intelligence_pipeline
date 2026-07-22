SELECT * FROM {{ref("stg_fred_cpiaucsl")}} AS cpiaucsl
FULL OUTER JOIN {{ref('stg_fred_dgs2')}} AS dgs2 USING(date)
FULL OUTER JOIN {{ref('stg_fred_dgs10')}} AS dgs10 USING(date)
FULL OUTER JOIN {{ref('stg_fred_dgs30')}} AS dgs30 USING(date)
FULL OUTER JOIN {{ref('stg_fred_fedfunds')}} AS fedfunds USING(date)
FULL OUTER JOIN {{ref('stg_fred_gdp')}} AS gdp USING(date)
FULL OUTER JOIN {{ref('stg_fred_unrate')}} AS unrate USING(date)
FULL OUTER JOIN {{ref('stg_yfinance_spy')}} AS spy USING(date)