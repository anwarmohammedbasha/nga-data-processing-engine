import os
from dotenv import load_dotenv

load_dotenv()

postgres_user_name = os.getenv('postgres_user_name')
postgres_password = os.getenv('postgres_password')
postgres_host = os.getenv('postgres_host')
postgres_port = os.getenv('postgres_port')
postgres_db = os.getenv('postgres_db')

Postgres_DB_URI = f'postgresql://{postgres_user_name}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db}'