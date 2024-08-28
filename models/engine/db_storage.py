from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import sqlalchemy

from models.deposit import Deposit
from models.payments import Payment
from models import Base
class DBStorage():
    """Interacts with mysql database
    """
    __engine = None
    __session = None
    def __init__(self):
        """start the storage
        """
        MYSQL_USER = getenv('MYSQL_USER')
        MYSQL_PWD = getenv('MYSQL_PWD')
        MYSQL_HOST = getenv('MYSQL_HOST')
        MYSQL_DB = getenv('MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(MYSQL_USER,
                                             MYSQL_PWD,
                                             MYSQL_HOST,
                                             MYSQL_DB))

    def new(self, obj):
        """add object to current session
        """
        self.__session.add(obj)

    def save(self):
        """Puts the changes to the databases
        """
        self.__session.commit()

    def delete(self, obj):
        """removes element from database
        """
        if obj is not None:
            self.__session.delete(obj)

    def close(self):
        """closes the session by calling remove
        """
        self.__session.remove()

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session
