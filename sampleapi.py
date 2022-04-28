import json

# def json_serial(obj):
#     from datetime import date, datetime
#     """JSON serializer for objects not serializable by default json code"""

#     if isinstance(obj, (datetime, date)):
#         return obj.isoformat()
#     raise TypeError ("Type %s not serializable" % type(obj))
def senddata(url,data):
    import requests
    url=url
    data=data
    r=requests.post(url,json=data)
    return r
# IP="" #request.META.get("REMOTE_ADDR")
def sendapi():
    import datetime
    #actually this is main date format when it will run there is a problem json serialization
    d = datetime.datetime.strptime("2017-10-13T10:53:53.000Z", "%Y-%m-%dT%H:%M:%S.000Z")
    #time=d.now()
    dd=datetime.datetime.now()
    #this is text format
    time=dd.strftime("%d/%m/%Y %H:%M:%S")
    url1="https://100003.pythonanywhere.com/eventcreation"
    data={"platformcode":"FB" ,"citycode":"101","daycode":"0",
                "dbcode":"pfm" ,"ip_address":"127.0.0.1",
                "login_id":"dowell_user6","session_id":"demo_user6",
                "processcode":"1","regional_time":time,
                "dowell_time":d.now(),"location":"22446541",
                "objectcode":"1","instancecode":"10003","context":"rad1",
                "document_id":"8990","rules":"you and me rules","status":"work1"
                }
    #try :
    l=senddata(url1,data)
    print(l.text)
   # except:
    #    print("server not found")
sendapi()
