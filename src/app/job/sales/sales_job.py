import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../')))

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

    print("Preview of validated data:")
    print(sales.head())

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

if __name__ == '__main__':
    # Using the relative path structure to find the data file
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
    csv_path = os.path.join(base_path, 'data', 'sales.csv')
    
    # If running on local Windows environment as per provided paths:
    # csv_path = 'E:/nga-data-processing-engine/data/sales.csv'
    sales_job(path=csv_path)