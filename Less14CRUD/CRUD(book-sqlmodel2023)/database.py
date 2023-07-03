from sqlmodel import SQLModel,create_engine
import os

# BASE_DIR=os.path.dirname(os.path.realpath(__file__))
# DB_URL = 'sqlite:///'+BASE_DIR+'/books.db'
# conn_str = 'sqlite:///'+os.path.join(BASE_DIR,'books.db')

#DATABASE_URL = "postgresql://user:password@postgresserver/db"
#conn_str = "postgresql://user:password@postgresserver/db" #local

from dotenv import load_dotenv
load_dotenv()#load .env
password : str = os.getenv('PASSWORD')
db_id : str = os.getenv('DBID')
conn_str = f"postgresql://postgres:{password}@db.{db_id}.supabase.co:6543/postgres"

print(conn_str)

engine=create_engine(conn_str,echo=True)