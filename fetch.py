#import the function fetch_fields_from_db
from targeted_population import fetch_fields_from_db

#database details
database_name='mongodb'
database='Bangalore'
collection='userdetails'
#specify the fields to be fetched
fields=['_id','event_id']

#call the fetch_fields_from_db function with start point and end point
start_point=27588500

end_point = 28465936

data=fetch_fields_from_db(database_name, fields,collection, database, start_point, end_point)
print(data)