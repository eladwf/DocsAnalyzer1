import MySQLdb

class SqlHandler(object):
    """description of class"""
    def __init__(self, **kwargs):
        self.connection = MySQLdb.connect (host = "localhost",
                              user = "elad",
                              passwd = "253545",
                              db = "docs")
        self.cursor = self.connection.cursor()
        #cursor.execute ("SELECT VERSION()")
        #row = cursor.fetchone()
        #cursor.close()
        return super().__init__(**kwargs)
    def insert(self,cword,param):
        inser="INSERT INTO `cwords` (`id`,`name`,`type`) VALUES (%d,'%s','%s')"%(2,'test','string')
        self.cursor.execute(inser)
        self.connection.commit()
        #execute sql insert
        return 1
    def select(self,cword,param):
        #execute sql select command
        self.cursor.execute("SELECT * FROM cwords")
        self.cursor.fetchall()
        self.cursor.close()
        return 1


