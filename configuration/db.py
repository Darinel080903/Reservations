from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

connection = os.getenv('URR1')
user = os.getenv('USS1')
password = os.getenv('PSS1')

engine = create_engine(f'mysql+pymysql://{user}:{password}@{connection}:3306/reservation', pool_size=10, max_overflow=20, pool_recycle=300)
meta = MetaData()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
conn = engine.connect()
