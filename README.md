# Event Creation API

#### Url: https://100003.pythonanywhere.com/event_creation
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
      "colour":"color value",
      "hashtags":"hash tag alue",
      "mentions":"mentions value",
      "emojis":"emojis",
      "bookmarks": "a book marks"
}

```
### for the values
		Platform			
			Input variable from master database in mysql		
		City			
			Input variable from master database in mysql		
		Day			
			Input variable from master database in mysql		
		Database 			
			Input variable from master database in mysql		
		IP Address			
			Call dowell track my IP function		
		Login ID			
			Call DowellLogin function		
		Session ID			
			Call DowellLogin function		
		Process 			
			Input variable from master database in mysql		
		Regional time			
			Call Dowell Clock function		
		Dowell time			
			Call Dowell Clock function		
		Location(GPS)			
			Call Dowell track my IP function		
		Object/form/flow			
			Input variable from master database in mysql		
		Instance ID			
			Input variable from the function 		
		Context			
			Input array from the function 		
		Document ID			
			Input variable from the function		

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
        "colour":"color value",
        "hashtags":"hash tag alue",
        "mentions":"mentions value",
        "emojis":"emojis",
        "bookmarks": "a book marks"
    }


    r=requests.post(url,json=data)
    print(r.text)
    
 ```
 
 ### Response:
 for success: {"is_success":true,"event_id":"FB1010000000000000000000003004","inserted_id":"63d0fca722375cb0dc8e336f"}
 for error: {"is_success":true,"event_id":"FB1010000000000000000000003004","inserted_id":"63d0fca722375cb0dc8e336f"}
 
 
 
