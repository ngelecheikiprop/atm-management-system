from os import getenv
from sqlalchemy import create_engine, func
from sqlalchemy.orm import scoped_session, sessionmaker
import sqlalchemy

from models.deposit import Deposit
from models.payments import Payment
from models.dispensed import Dispensed
from models import Base

name2class = {
        "Payment":Payment,
        "Dispensed":Dispensed,
        "Deposit":Deposit
        }
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
    
    def getthetwo(self):
        query = (
            self.__session.query(
                Payment.phone_number,
                Payment.transaction_id,
                Payment.initiation_id,
                Payment.time_received,
                Payment.amount,
                Dispensed.litres_dispensed,
                Dispensed.status
            )
            .join(Dispensed, Payment.initiation_id == Dispensed.initiation_id)
        )

        # Execute the query
        results = query.all()
        """
        print(results)
        # Display results
        for result in results:
            print(result)
        """ 
        # Define the date format you want
        date_format = "%Y-%m-%d %H:%M:%S"
        # Convert results to a list of dictionaries with formatted date
        result_list = [
                {
                    'phone_number': result.phone_number,
                    'transaction_id': result.transaction_id,
                    'initiation_id': result.initiation_id,
                    'time_received': result.time_received.strftime(date_format) if result.time_received else None,
                    'amount': result.amount,
                    'litres_dispensed': result.litres_dispensed,
                    'status': result.status
                    }
                for result in results
                ]
        return result_list
    
    def get_sum_of(self, table_column):
        """Returns the sum of a column from a given table"""
        table, column = table_column.split('.')
        table_class = globals()[table]  # Dynamically get the table class
        total_sum = self.__session.query(func.sum(getattr(table_class, column))).scalar()
        #return total_sum
        return int(total_sum) if total_sum is not None else 0
    
    def get_joined_columns(self, table1_column, table2_column):
        """Joins two tables and returns a list of dictionaries"""
        table1, column1 = table1_column.split('.')
        table2, column2 = table2_column.split('.')
        table1_class = globals()[table1]  # Dynamically get the table classes
        table2_class = globals()[table2]

        results = self.__session.query(table1_class, table2_class).filter(
            getattr(table1_class, column1) == getattr(table2_class, column2)).all()

        joined_data = []
        for row1, row2 in results:
            row_dict = {}
            for key in row1.__table__.columns.keys():
                row_dict[key] = getattr(row1, key)
            for key in row2.__table__.columns.keys():
                row_dict[key] = getattr(row2, key)
            joined_data.append(row_dict)
        return joined_data
    
    def get_joined_tables(self, table1, table2):
        """Joins two tables on their primary-foreign key relationship and returns a list of dictionaries"""
        # Dynamically get the table classes
        table1_class = name2class[table1]
        table2_class = name2class[table2]

        # Perform a join based on the primary-foreign key relationship
        # This assumes there is a direct relationship defined in the models
        results = self.__session.query(table1_class).join(table2_class).all()
        joined_data = []
        print(results)
        for row in results:
            print(row)
            print(row.__table__.columns.keys())
            row_dict = {}
            for key in row.__table__.columns.keys():
                row_dict[key] = getattr(row, key)
            print(row_dict)
            print( table2_class.__name__.lower())
            for related_row in getattr(row, table2_class.__name__.lower()):
                for key in related_row.__table__.columns.keys():
                    row_dict[key] = getattr(related_row, key)
            joined_data.append(row_dict)
        return joined_data

