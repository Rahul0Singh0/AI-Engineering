import os # Import the os module
from dotenv import load_dotenv # Import the load_dotenv function from the dotenv module

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from urllib.parse import quote_plus

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL") # Get the DATABASE_URL environment variable

engine = create_engine(DATABASE_URL) # create a sqlalchemy engine

# What is an sql alchemy engine ?
# An Engine is a factory for connection objects. It encapsulates a connection pool that minimizes the cost of connecting to the database by reusing existing connections and provides a cosistent API for working with transactions.

metadata = MetaData() # Create a SQLAlchemy MetaData object

Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # Create a SQLAlchemy sessionmaker object

Base = declarative_base() # Create a SQLAlchemy declarative base object