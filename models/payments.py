"""Stores the transactions completed
"""
class Payment(Base):
    """Defines the table to store transactions completed
    """
    __tablename__ = "payments"
    phone_number = Column(String(11), nullable=False)
    transaction_id = Column(String(50), nullable=False)
    initiation_id = Column(String(50), nullable=False, primary_key=True)
    amount = Column(Integer, nullable=False)
    time_received = Column(DateTime, default=datetime.now, nullable=False) 
