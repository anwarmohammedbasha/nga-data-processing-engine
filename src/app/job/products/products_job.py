import pandas as pd
from sqlalchemy import create_engine, text
from src.app.job.products.models.products import Products
from src.app.interface.config import Postgres_DB_URI

engine = create_engine(Postgres_DB_URI) 


def product_job(path):
    
    # Extract data from csv
    raw = pd.read_csv(path)


    # Validation 

    records = raw.to_dict(orient='records') # List of Dictonary



    validated_date = []
    for record in records:                          # for Each row
        validated = Products(**record)             # Validate
        validated_date.append(validated.model_dump())

    products = pd.DataFrame(validated_date)



    with engine.begin() as conn:
        # Delete records
        conn.execute(text('TRUNCATE TABLE NGA_PRODUCTS_TBL'))
        print('Reocords Deleted')
        # Ingest records
        products.to_sql(
            con=conn,
            name='nga_products_tbl',
            schema='public',    
            if_exists = 'append',
            index = False
        )
        print('Data Loaded to DB')
