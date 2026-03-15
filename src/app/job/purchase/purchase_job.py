import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../')))

import pandas as pd
from sqlalchemy import create_engine, text
from src.app.job.purchase.models.purchase import Purchase
from src.app.interface.config import Postgres_DB_URI

engine = create_engine(Postgres_DB_URI) 


def purchase_job(path):
    
    # Extract data from csv
    raw = pd.read_csv(path, parse_dates=True)


    # Validation 

    records = raw.to_dict(orient='records') 



    validated_date = []
    for record in records:
        validated = Purchase(**record)
        validated_date.append(validated.model_dump())

    purchase = pd.DataFrame(validated_date)

    with engine.begin() as conn:
        # Delete records
        conn.execute(text('TRUNCATE TABLE NGA_PURCHASE_TBL'))
        print('Reocords Deleted')
        # Ingest records
        purchase.to_sql(
            con=conn,
            name='nga_purchase_tbl',
            schema='public',    
            if_exists = 'append',
            index = False
        )
        print('Data Loaded to DB')

  
if __name__ == '__main__':
    purchase_job(path='E:/nga-data-processing-engine/data/purchase.csv')