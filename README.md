# Event Creation API

#### url: https://100003.pythonanywhere.com/event_creation
#### method: post

#### request data
```python

{
      "platformcode":"FB" ,
      "citycode":"101",
      "daycode":"0",
      "dbcode":"pfm" ,
      "ip_address":"192.168.0.41",
      "login_id":"lav",
      "session_id":"new",
      "processcode":"1",
      "regional_time":767677767,
      "dowell_time":781781278871,
      "location":"22446576",
      "objectcode":"1",
      "instancecode":"100051",
      "context":"afdafa ",
      "document_id":"3004",
      "rules":"some rules",
      "status":"work",
      "data_type": "learn",
      "purpose_of_usage": "add",
}

```

### Full example of calling event creation api:

```python
    dd=datetime.now()
    time=dd.strftime("%d:%m:%Y,%H:%M:%S")
    url="https://100003.pythonanywhere.com/event_creation"

    data={
        "platformcode":"FB" ,
        "citycode":"101",
        "daycode":"0",
        "dbcode":"pfm" ,
        "ip_address":"192.168.0.41",
        "login_id":"lav",
        "session_id":"new",
        "processcode":"1",
        "regional_time":time,
        "dowell_time":time,
        "location":"22446576",
        "objectcode":"1",
        "instancecode":"100051",
        "context":"afdafa ",
        "document_id":"3004",
        "rules":"some rules",
        "status":"work",
        "data_type": "learn",
        "purpose_of_usage": "add",
    }


    r=requests.post(url,json=data)
    
 ```
