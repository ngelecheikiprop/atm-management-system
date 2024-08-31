"""The functions that will recieve data from pi and store to database
"""
from sqlalchemy import Column, String, Float, Integer, DateTime, ForeignKey
from models import Base
from datetime import datetime

class Dispensed(Base):
    """Defines the dispensed table."""
    __tablename__ = "dispensed"
    initiation_id = Column(String(50), ForeignKey("payments.initiation_id"), nullable=False, primary_key=True)
    litres_dispensed = Column(Float, nullable=False)
    status = Column(String(50), nullable=False)
