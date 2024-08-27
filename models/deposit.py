"""milk deposits storage format
"""
class Deposit(Base):
    """Class to define milk desposits table
    """
    __tablename__ = "deposits"
    time_deposited = Column(DateTime, default=datetime.now, nullable=False)
    litres_deposited = Column(String(5), nullable=False, primary_key=True)
