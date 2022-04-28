# import MySQLdb
import sqlite3
import datetime

db = sqlite3.connect("db.sqlite3")
cursor = db.cursor()


class EventCreation:
    tableid = []
    input_var = {"instanceid": "", "context": "", "documentid": ""}
    # IP="" #request.META.get("REMOTE_ADDR")
    table = [
        "platform",
        "city",
        "day",
        "database",
        "process",
        "object",
    ]
    eventid = ""
    # To get sql connection
    db = sqlite3.connect("db.sqlite3")
    # db = MySQLdb.connect(host="localhost",    # your host, usually localhost
    #                      user="user",         # your username
    #                      passwd="pwd",  # your password
    #                      db="db")        # name of the data base

    # cursor that points to the db instance
    cursor = db.cursor()

    # Method to close the db connection
    def close_connection(self):
        self.cursor.close()
        sqlite3.connection.close()

    # Method to get correspondind id for the given table and code
    def get_id(self, table, code):
        query = f"SELECT * FROM {table} WHERE {table}_id='{code}';"
        self.cursor.execute(query)
        results = self.cursor.fetchone()
        if results:
            return "Yes"
        else:
            return "%s code not matching" % table

    # check input variable with db return the input value
    def check_db_values(self):
        count = 0
        countrev = 3
        while count < len(self.table):
            tb = self.table[count]
            value = input(f"Enter {self.table[count]} code :\t")
            fetch_value = self.get_id(tb, value)
            if fetch_value == "Yes":
                self.tableid.append(value)
                count += 1
            else:
                print(fetch_value)  # prompt for user
                # countrev-=1 #to limit user inputs
                # if countrev<=0:
                #     print("sorry try again")
                #     break
        if len(self.tableid) >= 1:
            for i in self.tableid:
                print(i)

    def get_new_values(self, function_value):
        if not function_value:
            print("is blank", end=" ")
            while True:
                function_value = input(function_value + "\t :")
                print(f"fill the value", end=" ")
                if function_value:
                    return function_value
                    break
        print(self.input_var)

    def create_function_value(self):
        for i in self.input_var:
            print(i, end=" ")
            self.input_var[i] = self.get_new_values(self.input_var[i])
        character = len(self.input_var["documentid"])
        if character < 24:
            self.input_var["documentid"] = self.input_var["documentid"].zfill(24)
        print(self.input_var)

    def insert(self):
        timeis = datetime.datetime.now()
        event_id = f"{self.tableid[0]}.{self.tableid[1]}.{self.tableid[2]}.{self.input_var['documentid']}"
        database_id = self.tableid[3]
        IP = "127.0.0.1"
        logindetails = "lav"
        sessiondetails = "fromd"
        process_id = self.tableid[4]
        regionaltime = timeis.strftime("%d:%m:%Y %H:%M:%S")
        dowelltime = "Get Server time"
        location = "location"
        object_id = self.tableid[5]
        instance_id = self.input_var["instanceid"]
        context = self.input_var["context"]
        try:
            query = """INSERT INTO DowellEventCreation(eventid,
                database_id,
                IP,
                logindetails,
                sessiondetails,
                process,
                regionaltime,
                dowelltime,
                location,
                object_id,
                instanceid,
                context)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?);"""
            values=(event_id,database_id,IP,logindetails,sessiondetails,process_id,
                    regionaltime,dowelltime,location,object_id,instance_id,context)
            count = cursor.execute(query,values)
            db.commit()
            print(
                "Record inserted successfully into SqliteDb_developers table ",
                cursor.rowcount,
            )
            cursor.close()
        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table", error)


obj = EventCreation()
obj.check_db_values()
obj.create_function_value()
obj.insert()