import pandas as pd
from sqlalchemy import create_engine, text
from src.app.job.sales.models.sales import Sales
from src.app.interface.config import Postgres_DB_URI

engine = create_engine(Postgres_DB_URI) 

def sales_job(path):
    # Extract data from csv
    # Note: specifying dayfirst=True because date format is 19-04-2024
    raw = pd.read_csv(path, parse_dates=['order_date'], dayfirst=True)

    # Validation 
    records = raw.to_dict(orient='records') 

    validated_data = []
    for record in records:
        validated = Sales(**record)
        validated_data.append(validated.model_dump())

    sales = pd.DataFrame(validated_data)



    with engine.begin() as conn:
        # Delete records
        conn.execute(text('TRUNCATE TABLE NGA_SALES_TBL'))
        print('Records Deleted')
        
        # Ingest records
        sales.to_sql(
            con=conn,
            name='nga_sales_tbl',
            schema='public',    
            if_exists='append',
            index=False
        )
        print('Data Loaded to DB')
    