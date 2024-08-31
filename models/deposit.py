"""milk deposits storage format
"""
from sqlalchemy import Column, String, Integer, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

from models import Base
class Deposit(Base):
    """Class to define milk desposits table
    """
    __tablename__ = "deposits"
    id = Column(Integer, primary_key=True, autoincrement=True)
    time_deposited = Column(DateTime, default=datetime.now, nullable=False)
    litres_deposited = Column(String(5), nullable=False)
