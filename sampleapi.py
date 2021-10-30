def senddata(url,data):
    import requests
    url=url
    data=data
    r=requests.post(url,json=data)
    return r
def sendapi():
    from datetime import datetime
    dd=datetime.now()
    #new
    time=dd.strftime("%d:%m:%Y,%H:%M:%S")
    url1="https://100003.pythonanywhere.com/eventcreation"
    data={"platformcode":"FB" ,"citycode":"101","daycode":"0",
                "dbcode":"pfm" ,"ip_address":"127.0.0.1",
                "login_id":"lav","session_id":"new",
                "processcode":"1","regional_time":time,
                "dowell_time":time,"location":"224465",
                "objectcode":"1","instancecode":"10001","context":"rad",
                "document_id":"3003"
                }
    try :
        l=senddata(url1,data)
        print(l.text)
    except:
        print("server not found")
sendapi()
