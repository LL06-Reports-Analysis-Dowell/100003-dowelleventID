
# A very simple Flask Hello World app for you to get started with...

from flask import Flask , request ,jsonify,url_for,session,render_template
from dowellconnection import dowellconnection
#from encrypt import AESCipher
app = Flask(__name__)
import json
import base64
import certifi
from bson import ObjectId
#from datetime import datetime
import datetime
dd=datetime.datetime.now()
time=dd.strftime("%d/%m/%Y %H:%M:%S")
def timefun():
    dd=datetime.datetime.now()
    time=dd.strftime("%d:%m:%Y,%H:%M:%S")
    return time
d = datetime.datetime.strptime("2017-10-13T10:53:53.000Z", "%Y-%m-%dT%H:%M:%S.000Z")
#import re
def dowellclock():
        oldt=1609459200
        import time
        t1=time.time()
        dowell=t1-oldt
        return dowell

# @app.route('/', methods =["GET", "POST"])
# def dowellevents():
#     if (request.method=="POST"):
#         request_data=request.get_json()
#         platformcode = request_data['platformcode']
#         citycode= request_data['citycode']
#         daycode= request_data['daycode']
#         dbcode= request_data['dbcode']
#         ip_address= request_data['ip_address']
#         login_id=request_data['login_id']
#         session_id=request_data['session_id']
#         processcode = request_data['processcode']
#         regional_time=request_data['regional_time']
#         dowell_time=request_data['dowell_time']
#         location=request_data['location']
#         objectcode=request_data['objectcode']
#         instance_id = request_data['instancecode']
#         context = request_data['context']
#         document_id = request_data['document_id']


#         field={"platformcode":platformcode }
#         response=dowellconnection("mstr","bangalore","mysql","platform_master","pfm_master","97654321","ABCDE","fetch",field,"nil")
#         if response != "null":
#             platform_ID=response
#         else:
#             error = {"number": 0,"description": "Platform is not matching"}
#             return error

#         field={"citycode":citycode}
#         response=dowellconnection("mstr","bangalore","mysql","city_master","city_master","67654321","ABCDE","fetch",field,"nil")
#         if response != "null":
#             city_ID=response
#         else:
#             error = {"number": 0,"description": "city code is not matching"}
#             return error

#         field={"daycode":daycode }
#         response=dowellconnection("mstr","bangalore","mysql","day_master","day_master","77654321","ABCDE","fetch",field,"nil")
#         if response != "null":
#             day_ID =response
#         else:
#             error = {"number": 0,"description": "day code is not matching"}
#             return error

#         field={"dbcode":dbcode }
#         response=dowellconnection("mstr","bangalore","mysql","db_master","db_master","37654321","ABCDE","fetch",field,"nil")
#         if response != "null":
#             db_ID =response
#         else:
#             error = {"number": 0,"description": "database code is not matching"}
#             return error

#         field={"processcode":processcode }
#         response=dowellconnection("mstr","bangalore","mysql","process_master","process_master","57654321","ABCDE","fetch",field,"nil")
#         if response != "null":
#             process_ID=response
#         else:
#             error = {"number": 0,"description": "Process code is not matching"}
#             return error

#         field={"objectcode":objectcode }
#         response=dowellconnection("mstr","bangalore","mysql","object_master","object_master","47654321","ABCDE","fetch",field,"nil")
#         if response != "null":
#             object_ID =response
#         else:
#             error = {"number": 0,"description": "Object code is not matching"}
#             return error
#         """
#         field={"instancecode":instancecode }
#         response=dowellconnection.dowellconnection("FB","bangalore","mysql","object_master","qr","654321","EDCBA","fetch",field,"nil")
#         if response != "null":
#             instance_ID =response
#         else:
#             error = {"number": 0,"description": "Instance code is not null"}
#             return error

#         """
#         if not instance_id:
#             error = {"number": 0,"description": "'Instance Id is null'"}
#             return error
#         if isinstance(context, list) and not context:
#             error = {"number": 0,"description": "context is empty"}
#             return error

#         if len(document_id)<24:
#             document_id=document_id.zfill(24-len(document_id)) # To fill prefix with zero to make length to 24
#         if len(document_id)>24:
#             error = {"number": 0,"description": "Invalid document id"}
#             return error

#         event_id=platform_ID+city_ID+day_ID+document_id
#         if len(event_id) !=33:
#             error = {"number": 0,"description": event_id+"Error in Event Id Creation"}
#             return error


#         field = {"eventId":event_id ,"DatabaseId":db_ID ,"IP":ip_address,"login":login_id ,"session":session_id,"process":process_ID,"regional_time":regional_time,"dowell_time":dowell_time,"location":location,"object":object_ID,"instane_id":instance_id,"context": context}
#         NewObjectID=dowellconnection("FB","bangalore","mongodb","events","events","87654321","ABCDE","insert",field,"nil")
#         #retstring = NewObjectID + event_id
#         retstring = 'NewObjectID'+':'+NewObjectID+ '\n' +'event_id'+':'+event_id
#         #return JSONEncoder().encode(retstring)
#         #return {"NewObjectID": str(NewObjectID) , "event_id": str(event_id)}
#         return retstring
@app.route('/eventcreation',methods =["GET", "POST"])
def api_data():
    if (request.method=="POST"):
        pfm_id=""
        city_id=""
        day_id=""
        db_id=""
        process_id=""
        object_id=""
        request_data=request.get_json()
        pfm_code = request_data['platformcode']
        pfm={"platformcode":pfm_code}
        pfm_response=dowellconnection("mstr","bangalore","pfm","platform_master","pfm_master","97654321","ABCDE","fetch",pfm,"nil")
        if not pfm_code in pfm_response or pfm_response=="false":
            return "Platform code not matching"
           # return pfm_response
        else:
            #city_ID=re.findall('\d+',response)[0]
            pfm_id=pfm_code
        timer=timefun()
        city_code = request_data['citycode']
        city={"citycode":city_code}
        city_response=dowellconnection("mstr","bangalore","pfm","city_master","city_master","67654321","ABCDE","fetch",city,"nil")
        if not city_code in city_response or city_response=="false":
            return "City code not matching"
        else:
            city_id=city_code
        day_code = request_data['daycode']
        day={"daycode":day_code}
        day_response=dowellconnection("mstr","bangalore","pfm","day_master","day_master","77654321","ABCDE","fetch",day,"nil")
        if not day_code in day_response or day_response=="false":
            return "day code not matching"
        else:
            day_id=day_code
        db_code = request_data['dbcode']
        db={"dbcode":db_code}
        db_response=dowellconnection("mstr","bangalore","pfm","db_master","db_master","37654321","ABCDE","find",db,"nil")
        if not db_code in db_response or db_response=="false":
            return "database code not matching"
        else:
            db_id=db_code
        process_code = request_data['processcode']
        process={"processcode":process_code}
        process_response=dowellconnection("mstr","bangalore","pfm","process_master","process_master","57654321","ABCDE","fetch",process,"nil")
        if not process_code in process_response or process_response=="false":
            return "process code not matching"
        else:
            process_id=process_code
        object_code = request_data['objectcode']
        object={"objectcode":object_code}
        object_response=dowellconnection("mstr","bangalore","pfm","object_master","object_master","47654321","ABCDE","fetch",object,"nil")
        if not object_code in object_response or object_response=="false":
            return "object code not matching"
        else:
            object_id=object_code
        instance=request_data["instancecode"]
        if not instance:
            return "Instance is blank fill again"
        else:
            instance_id=instance
        Context=list(request_data["context"])
        if not request_data["rules"]:
            return "rules is blank fill again"
        else:
            rules=request_data["rules"]
        if not Context:
            return "Context is blank"
        else:
            context_is=[request_data["context"],rules,object_id,request_data["login_id"],timer]
        document=request_data["document_id"]
        if not document:
            return "Document is blank"
        else:
            if len(request_data["document_id"])>24:
                return "Invalid document id"
            elif len(request_data["document_id"])<24:
                document=document.zfill(24) # To fill prefix with zero to make length to 24
                document_id=document
        event_id=pfm_id+city_id+day_id+document_id
        status=request_data["status"]
        if not status:
            return "status is blank fill again"
        else:
            status_field=status
        if len(event_id) !=30:
            return "Error while creating Event ID"
        else:
            #newdate=datetime.datetime.strptime(request_data["dowell_time"], '%d/%m/%Y %H:%M:%S')
            #ls=[pfm_id,city_code,day_id,db_id,request_data["IP_Address"],request_data["login"],request_data["session"],process_id,
            #request_data["regional_time"],request_data["dowell_time"],request_data["location"],object_id,instance_id,context,document_id]
            field = {"eventId":event_id ,
            "DatabaseId":db_id ,"IP":request_data["ip_address"],
            "login":request_data["login_id"],"session":request_data["session_id"],
            "process":process_id,"regional_time":request_data["regional_time"],
            "dowell_time":request_data["dowell_time"],"location":request_data["location"],
            "object":object_id,"instane_id":instance_id,"context": context_is,"status":status_field}
            NewObjectID=dowellconnection("FB","bangalore","blr","events","events","87654321","ABCDE","insert",field,"nil")
            return f"NewObjectID : {NewObjectID} \n event_id :{event_id}"
    return "page works"

@app.route('/events',methods =["GET", "POST"])
def form_data():
    context={}
    if (request.method=="POST"):
        pfm_id="01"
        city_id="101"
        day_id="1001"
        db_id="01"
        process_id="01"
        object_id="01"
        request_data=request.form.to_dict()
        context["ls1"]=request_data
        pfm_code = request_data['pfm_code']
        pfm={"platformcode":pfm_code}
        pfm_response=dowellconnection("mstr","bangalore","pfm","platform_master","pfm_master","97654321","ABCDE","fetch",pfm,"nil")
        if not pfm_code in pfm_response or pfm_response=="false":
            pfm_code_error="Platform code not matching"
            context["pfm_error"]=pfm_code_error
            #return redirect(url_for('index'))
        else:
            #city_ID=re.findall('\d+',response)[0]
            pfm_id=pfm_code
        city_code = request_data['city_code']
        city={"citycode":city_code}
        city_response=dowellconnection("mstr","bangalore","pfm","city_master","city_master","67654321","ABCDE","fetch",city,"nil")
        if not city_code in city_response or city_response=="false":
            city_code_error="City code not matching"
            context["city_error"]=city_code_error
        else:
            city_id=city_code
            context["lav"]=city_id
        day_code = request_data['day_code']
        day={"daycode":day_code}
        day_response=dowellconnection("mstr","bangalore","pfm","day_master","day_master","77654321","ABCDE","fetch",day,"nil")
        if not day_code in day_response or day_response=="false":
            day_code_error="day code not matching"
            context["day_error"]=day_code_error
        else:
            day_id=day_code
        db_code = request_data['database_code']
        db={"dbcode":db_code}
        db_response=dowellconnection("mstr","bangalore","pfm","db_master","db_master","37654321","ABCDE","fetch",db,"nil")
        if not db_code in db_response or db_response=="false":
            db_code_error="database code not matching"
            context["database_error"]=db_code_error
        else:
            db_id=db_code
        process_code = request_data['process_code']
        process={"processcode":process_code}
        process_response=dowellconnection("mstr","bangalore","pfm","process_master","process_master","57654321","ABCDE","fetch",process,"nil")
        if not process_code in process_response or process_response=="false":
            process_code_error="process code not matching"
            context["process_error"]=process_code_error
        else:
            process_id=process_code
        object_code = request_data['object_code']
        object={"objectcode":object_code}
        object_response=dowellconnection("mstr","bangalore","pfm","object_master","object_master","47654321","ABCDE","fetch",object,"nil")
        if not object_code in object_response or object_response=="false":
            object_code_error="object code not matching"
            context["object_error"]=object_code_error
        else:
            object_id=object_code
        if not request_data["instance_id"]:
            instance_code_error="Instance is blank fill again"
            context["instance_error"]=instance_code_error
        else:
            instance_id=request_data["instance_id"]
        Context=list(request_data["context"])
        if not request_data["rules"]:
            context["rules_error"]="rules is blank fill again"
        else:
            rules=request_data["rules"]
        if not Context:
            context["context_error"]="Context is blank"
        else:
            context_is=[request_data["context"],rules,object_id,request_data["login"],time]
        if not request_data["document_id"]:
            document_code_error="Document is blank"
            context["document_error"]=document_code_error
        else:
            if len(request_data["document_id"])>24:
                document_code_error="Invalid document id"
                context["document_error"]=document_code_error
            elif len(request_data["document_id"])<24:
                request_data["document_id"]=request_data["document_id"].zfill(24) # To fill prefix with zero to make length to 24
                document_id=request_data["document_id"]
        status=request_data["status"]
        if not status:
            context["status_error"]="status is blank fill again"
        else:
            status_field=status
        event_id=pfm_id+city_id+day_id+document_id
        if len(event_id) !=30:
            context["event_error"] = "Error while creating Event ID"
        else:
            #ls=[pfm_id,city_code,day_id,db_id,request_data["IP_Address"],request_data["login"],request_data["session"],process_id,
            #request_data["regional_time"],request_data["dowell_time"],request_data["location"],object_id,instance_id,context,document_id,status]
            field = {"eventId":event_id ,
            "DatabaseId":db_id ,"IP":request_data["IP_Address"],
            "login":request_data["login"],"session":request_data["session"],
            "process":process_id,"regional_time":d.now(),
            "dowell_time":request_data["dowell_time"],"location":request_data["location_code"],
            "object":object_id,"instane_id":instance_id,"context": context,"status":status}
            NewObjectID=dowellconnection("FB","bangalore","blr","events","events","87654321","ABCDE","insert",field,"nil")
            context["retstring"] = 'NewObjectID'+':'+NewObjectID+ '\n' +'event_id'+':'+event_id
    context["IP"]=request.remote_addr
    context["session"]=session.get("form_data")
    context["time"]=time

    return render_template("index.html",context=context)
@app.route('/testevent',methods =["GET", "POST"])
def event():
    context={}
    import urllib.request
    from event_function import event_creation
    if (request.method=="POST"):
        with urllib.request.urlopen("https://geolocation-db.com/json",cafile=certifi.where()) as url:
            data = json.loads(url.read().decode())
            context["ipdetails"]=data
        request_data=request.form.to_dict()
        name=request_data["name"]
        email=request_data["email"]
        IP=request.remote_addr
        context["ip"]=IP
        event_id=event_creation("FB","101","0","pfm","1","1","1029"," dafafthis is some text fadf","new rulesfd",name,"5029","progress",data["IPv4"],"session",data["city"])
        field={
            "name":name,
            "email":email,
            "event_id":event_id,
            "time":time
        }
        obj=dowellconnection("FB","bangalore","blr","userdetails","userdetails","7654890","ABCDE","insert",field,"nil")
        #context["id"]=obj
        context["event_id"]=event_id
    return render_template("lav.html",context=context)


@app.route('/event_creation',methods =["GET", "POST"])
def event_call():
    context={}
    import urllib.request
    from event_function import event_creation
    if (request.method=="POST"):
        request_data=request.get_json()
        data={"platformcode":"FB" ,"citycode":"101","daycode":"0",
                "dbcode":"pfm" ,"ip_address":"127.0.0.1",
                "login_id":"lav","session_id":"new",
                "processcode":"1","regional_time":time,
                "dowell_time":time,"location":"224465",
                "objectcode":"1","instancecode":"10001","context":"rad",
                "document_id":"3003","rules":"some rules","status":"work"
                }
        data_type = request_data.get("data_type", "")
        purpose_of_usage = request_data.get("purpose_of_usage", "")
        colour = request_data.get("colour", "")
        hashtags = request_data.get("hashtags", "")
        mentions = request_data.get("mentions", "")
        emojis = request_data.get("emojis", "")

        event_id=event_creation(request_data["platformcode"],request_data["citycode"],request_data["daycode"],
            request_data["dbcode"],request_data["processcode"],request_data["objectcode"],request_data["instancecode"],
            request_data["instancecode"],request_data["rules"],request_data["login_id"],request_data["document_id"],
            request_data["status"],request_data["ip_address"], request_data["session_id"],request_data["location"],
            data_type, purpose_of_usage, colour, hashtags, mentions, emojis)
        return event_id
    return "its works"


@app.route('/dowelltime',methods =["GET", "POST"])
def dowellc():
    dowelltime=round(dowellclock())
    return f"dowell time : {dowelltime}"

@app.route('/fetchstart',methods =["GET", "POST"])
def fetchdata(context=None):
    from targeted_population import fetch_fields_from_db
    context={}
    if (request.method=="POST"):
        request_data=request.form.to_dict()
        start=str(request_data["start"])+":00"
        end=str(request_data["end"])+":00"
        print(start)
        print(3)
        print(3)
        print(end)
        s=datetime.datetime.strptime(start.replace("T"," "), "%Y-%m-%d %H:%M:%S").timestamp()
        e=datetime.datetime.strptime(end.replace("T"," "), "%Y-%m-%d %H:%M:%S").timestamp()
        #r=time.strftime('%d/%m/%Y %H:%M:%S', time.localtime(27514894))
        #database details
        database_name='mongodb'
        database='Bangalore'
        collection='userdetails'
        #specify the fields to be fetched
        fields=['_id','name','email']

        #call the fetch_fields_from_db function with start point and end point
        start_point=round(s)
        end_point = round(e)
        data=fetch_fields_from_db(database_name, fields,collection, database, start_point, end_point)
        context["data"]=data
        context["start"]=start_point
        context["end"]=end_point
    return render_template("lav1.html",context=context)

@app.route('/android',methods =["GET", "POST"])
def Android():
    if (request.method=="POST"):
        dic={}
        request_data=request.form.to_dict()
        dic["message"]="str"
        # enstr=name.encode()
        # destr=base64.b64decode(enstr)
        # strorig=destr.decode()
        # name1=strorig.replace("'", "\"")
        # #name1=name.replace("'", "\"")
        # jsontodic=json.loads(name1)
        # try:
        #     field={"order_id": str(jsontodic["order_id"])}
        #     conn_fetch=dowellconnection("qr","bangalore","qrcode_demo_app","app_data","app_data","2387654311","ABCDE","find",field,"nil")
        #     fetch_item=json.loads(conn_fetch)
        #     field1={"item_id": fetch_item["item_id"]}
        #     conn=dowellconnection("qr","bangalore","qrcode_demo_app","app_data","app_data","2387654311","ABCDE","find",field1,"nil")
        #     fetch_items=json.loads(conn)
        #     number=int(fetch_items["waiting_status"])
        #     while True:
        #         rquery={"item_id": fetch_item["item_id"],"waiting_status":str(number)}
        #         rr=dowellconnection("qr","bangalore","qrcode_demo_app","app_data","app_data","2387654311","ABCDE","find",rquery,"nil")
        #         if rr!="null":
        #             query1={"item_id": fetch_item["item_id"],"waiting_status":str(number)}
        #             update={"waiting_status": str(number-1)}
        #             conn=dowellconnection("qr","bangalore","qrcode_demo_app","app_data","app_data","2387654311","ABCDE","update",query1,update)
        #         else:
        #             break
        #     query={"order_id": str(jsontodic["order_id"])}
        #     update={"waiting_status": "0","delivery_status": "Yes"}
        #     conn_update=dowellconnection("qr","bangalore","qrcode_demo_app","app_data","app_data","2387654311","ABCDE","update",query,update)
        #     dic["message"]="Order delivered"
        #     return jsonify(dic)
        # except:
        #     dic["message"]="An error occurred while updating"
        return jsonify(dic)
        # try:
        #     while True:
        #         rquery={"item_id": fetch_item["item_id"],"waiting_status":str(number)}
        #         rr=dowellconnection("qr","bangalore","qrcode_demo_app","app_data","app_data","2387654311","ABCDE","find",rquery,"nil")
        #         if rr!="null":
        #             query1={"item_id": fetch_item["item_id"],"waiting_status":str(number)}
        #             update={"waiting_status": str(number-1)}
        #             conn=dowellconnection("qr","bangalore","qrcode_demo_app","app_data","app_data","2387654311","ABCDE","update",query,update)
        #         else:
        #             break
        #     query={"order_id": jsontodic["order_id"]}
        #     update={"waiting_status": "0","delivery_status": "Yes"}
        #     conn_update=dowellconnection("qr","bangalore","qrcode_demo_app","app_data","app_data","2387654311","ABCDE","update",query,update)
        #     dic["message"]=conn_update
        #     return jsonify(dic)
        # except:
        #     dic["message"]="an error occurred while update"
        #     return jsonify(dic)
    return "it works"

#fill using html form
# @app.route('/form',methods =["GET", "POST"])
# def index1(context=None):
#     context={}
#     if (request.method=="POST"):
#         request_data=request.form.to_dict()
#         value = request_data['value']
#         objects = request_data['object']
#         rule = request_data['rules']
#         login = request_data['login']
#         if value and objects and rule and login:
#             context["value"]=value
#             context["object"]=objects
#             context["rule"]=rule
#             context["login"]=login
#             timer=timefun()
#             context["time"]=timer
#             field = {"somevalue":value,"modified date":timer,"objects":objects,"rule":rule,"login":login}
#             #create=dowellconnection("FB","bangalore","blr","events","events","87654321","ABCDE","insert",field,"nil")
#         else:
#             context["err"]="Input is blank"
#     return render_template("create.html",context=context)
#fill using html form
# @app.route('/timefun',methods =["GET", "POST"])
# def timefunc():
#     if (request.method=="POST"):
#         request_data=request.get_json()
#         value = request_data['value']
#         objects = request_data['object']
#         rule = request_data['rules']
#         login = request_data['login']
#         if value and objects and rule and login:
#             timer=timefun()
#             field = {"somevalue":value,"modified date":timer,"objects":objects,"rule":rule,"login":login}
#             create=dowellconnection("FB","blr","mongodb","events","events","87654321","ABCDE","insert",field,"nil")
#             return "data successfully sent"
#         else:
#             return "could not insert data into the database"
#     return "it works"
# with app.test_request_context():
#     print(url_for('index'))

# with app.test_request_context():
#     print(url_for('index'))
# if __name__=='__main__':
#     app.run(debug=True)
# class JSONEncoder(json.JSONEncoder):
#     def default(self, o):
#         if isinstance(o, ObjectId):
#             return str(o)
#         return json.JSONEncoder.default(self, o)


