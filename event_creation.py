import MySQLdb
class EventCreation:
    flatform_id=""
    city_id=""
    day_id=""
    database_id=""
    object_id=""
    #To get sql connection
    db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                         user="user",         # your username
                         passwd="pwd",  # your password
                         db="db")        # name of the data base

    #cursor that points to the db instance
    cursor = db.cursor()

    #Method to close the db connection
    def close_connection(self):
        self.cursor.close()
        MySQLdb.connection.close() 
    #Method to get correspondind id for the given table and code
    def get_id(self,table, code):
        query = "SELECT id FROM %s WHERE code='%s';"%(table,code)
        self.cursor.execute(query)
        results =self.cursor.fetchall()
        if results>1:
          return results
        else:
          return "%s code not matching"%code

