class SqlHandler(object):
    """description of class"""
    def __init__(self, **kwargs):
        connection = MySQLdb.connect (host = "localhost",
                              user = "testuser",
                              passwd = "testpass",
                              db = "company")
        cursor = connection.cursor()
        #cursor.execute ("SELECT VERSION()")
        #row = cursor.fetchone()
        cursor.close()
        return super().__init__(**kwargs)
    def insert(self,cword,param):
        #execute sql insert
        return 1
    def select(self,cword,param):
        #execute sql select command
        return 1


