from sqlalchemy import Column, String, Integer, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
Base = declarative_base()

from models.engine.db_storage import DBStorage
storage = DBStorage()
storage.reload()
