import json
import requests
from flask import Flask , request ,jsonify
from dowellconnection import dowellconnection
url = 'http://100003.pythonanywhere.com'

field={"processcode":1 }
response=dowellconnection("mstr","bangalore","mysql","process_master","process_master","57654321","ABCDE","find",field,"nil")
print(response)

