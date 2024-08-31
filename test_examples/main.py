#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+mysqldb://root:root@localhost/test_db")
Base = declarative_base()

class User(Base):
    __tablename__="users"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    nickname = Column(String(50))

class Address(Base):
    __tablename__='addresses'
    id = Column(Integer, primary_key=True)
    email_address=Column(String(50), nullable=False)
    user_id=Column(Integer, ForeignKey('users.id'))

#Base.metadata.create_all(engine)
"""
kiprop = User(name="kiprop", fullname="Kiprop ngelechei", nickname="solo")
"""
"""
ad = Address(email_address="ngkiprop@gmail.com", user_id=1)
chem= User(name="chem", fullname="Maryanne Chemutai", nickname="chemchem")
ad2 = Address(email_address="mchemchem@gmail.com", user_id=3)
"""
Session = sessionmaker(bind=engine)
session = Session()
"""
session.add_all([ad, chem, ad2])
session.commit()
"""
for u in session.query(User).join(Address).all():
    print(u.name, u.email)

