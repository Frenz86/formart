from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

BASE_DIR=os.path.dirname(os.path.realpath(__file__))
DB_URL = 'sqlite:///'+BASE_DIR+'/test.db'
print(DB_URL)
engine = create_engine(DB_URL, connect_args={'check_same_thread': False})

# import os
# from dotenv import load_dotenv
# load_dotenv()
# password : str = os.getenv('PASSWORD')
# db_id : str = os.getenv('DBID')
# conn_str = f"postgresql://postgres:{password}@db.{db_id}.supabase.co:6543/postgres"
# print(conn_str)
# engine=create_engine(conn_str,echo=True)
# ## popola la tabella user su SUPABASE

sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()