"""Stores the transactions completed
"""
from sqlalchemy import Column, String, Integer, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

from models import Base
class Payment(Base):
    """Defines the table to store transactions completed
    """
    __tablename__ = "payments"
    phone_number = Column(String(12), nullable=False)
    transaction_id = Column(String(50), nullable=False)
    initiation_id = Column(String(50), nullable=False, primary_key=True)
    amount = Column(Integer, nullable=False)
    time_received = Column(DateTime, default=datetime.now, nullable=False) 
