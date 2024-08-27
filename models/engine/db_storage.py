Class DBStorage():
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


