from flask import Flask,request,session,jsonify,url_for
from flask import render_template
#from werkzeug.utils import redirect
from dowellconnection import dowellconnection
from datetime import datetime
import json
dd=datetime.now()
time=dd.strftime("%d:%m:%Y,%H:%M:%S")
#import re
lav=Flask(__name__)
@lav.route('/events',methods =["GET", "POST"])
def index(context=None):
    context={}
    if (request.method=="POST"):
        pfm_id=""
        city_id=""
        day_id=""
        db_id=""
        process_id=""
        object_id=""
        request_data=request.form.to_dict()
        context["ls1"]=request_data
        pfm_code = request_data['pfm_code']
        pfm={"platformcode":pfm_code}
        pfm_response=dowellconnection("mstr","bangalore","mysql","platform_master","pfm_master","97654321","ABCDE","fetch",pfm,"nil")
        if not pfm_code in pfm_response or pfm_response=="false":
            pfm_code_error="Platform code not matching"
            context["pfm_error"]=pfm_code_error
            #return redirect(url_for('index'))
        else:
            #city_ID=re.findall('\d+',response)[0]
            pfm_id=pfm_code
        city_code = request_data['city_code']
        city={"citycode":city_code}
        city_response=dowellconnection("mstr","bangalore","mysql","city_master","city_master","67654321","ABCDE","fetch",city,"nil")
        if not city_code in city_response or city_response=="false":
            city_code_error="City code not matching"
            context["city_error"]=city_code_error
        else:

            city_id=city_code
            context["lav"]=city_id
        day_code = request_data['day_code']
        day={"daycode":day_code}
        day_response=dowellconnection("mstr","bangalore","mysql","day_master","day_master","77654321","ABCDE","fetch",day,"nil")
        if not day_code in day_response or day_response=="false":
            day_code_error="day code not matching"
            context["day_error"]=day_code_error
        else:
            day_id=day_code
        db_code = request_data['database_code']
        db={"dbcode":db_code}
        db_response=dowellconnection("mstr","bangalore","mysql","db_master","db_master","37654321","ABCDE","fetch",db,"nil")
        if not db_code in db_response or db_response=="false":
            db_code_error="database code not matching"
            context["database_error"]=db_code_error
        else:
            db_id=db_code
        process_code = request_data['process_code']
        process={"processcode":process_code}
        process_response=dowellconnection("mstr","bangalore","mysql","process_master","process_master","57654321","ABCDE","fetch",process,"nil")
        if not process_code in process_response or process_response=="false":
            process_code_error="process code not matching"
            context["process_error"]=process_code_error
        else:
            process_id=process_code
        object_code = request_data['object_code']
        object={"processcode":object_code}
        object_response=dowellconnection("mstr","bangalore","mysql","object_master","object_master","47654321","ABCDE","fetch",object,"nil")
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
        if isinstance(request_data["context"], list) and not request_data["context"]:
            context_code_error="Context is blank"
            context["context_error"]=context_code_error
        else:
            context_is=request_data["context"]
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
        event_id=pfm_id+city_id+day_id+document_id
        if len(event_id) !=33:
            context["event_error"] = "Error while creating Event ID"
        else:
            #ls=[pfm_id,city_code,day_id,db_id,request_data["IP_Address"],request_data["login"],request_data["session"],process_id,
            #request_data["regional_time"],request_data["dowell_time"],request_data["location"],object_id,instance_id,context,document_id]
            field = {"eventId":event_id ,
            "DatabaseId":db_id ,"IP":request_data["IP_Address"],
            "login":request_data["login"],"session":request_data["session"],
            "process":process_id,"regional_time":request_data["regional_time"],
            "dowell_time":request_data["dowell_time"],"location":request_data["location_code"],
            "object":object_id,"instane_id":instance_id,"context": context}
            NewObjectID=dowellconnection("FB","bangalore","mongodb","events","events","87654321","ABCDE","insert",field,"nil")
            context["retstring"] = 'NewObjectID'+':'+NewObjectID+ '\n' +'event_id'+':'+event_id
    context["IP"]=request.remote_addr
    context["session"]=session.get("index")
    context["time"]=time

    return render_template("index.html",context=context)

with lav.test_request_context():
    print(url_for('index'))
if __name__=='__main__':
    lav.run(debug=True)