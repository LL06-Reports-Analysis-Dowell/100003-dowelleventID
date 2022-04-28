import json
import requests

url = 'http://100003.pythonanywhere.com'

def dowellevent(platformcode,citycode,daycode,dbcode,ip_address,login_id,session_id,processcode,regional_time,dowell_time,location,objectcode,instancecode,context,document_id):
    #dowellevent("FB","101","0","1","106.51.110.198","login1","session1","1","222222","85466","BLR","1","10001",field,"60505661e0b9b354e134006d")
    data={
        "platformcode":platformcode,
        "citycode":citycode,
        "daycode":daycode,
        "dbcode":dbcode,
        "ip_address":ip_address,
        "login_id":login_id,
        "session_id":session_id,
        "processcode":processcode,
        "regional_time":regional_time,
        "dowell_time":dowell_time,
        "location":location,
        "objectcode":objectcode,
        "instancecode":instancecode,
        "context":context,
        "document_id":document_id
        }

    headers = {'content-type': 'application/json'}
    response = requests.post(url, json =data,headers=headers)
    return response.text


""" Script to call the event function"""
"""
@app.route('/e', methods =["GET", "POST"])
def callevent():
    context="buttonclick"
    field= {"context1":context}
            #dowellevent(platformcode,citycode,daycode,dbcode,ip_address,login_id,session_id,processcode,regional_time,dowell_time,location,objectcode,instancecode,context,document_id)
    NewObjectID=dowellevent("FB","101","0","pfm","106.51.110.198","login1","session1","1","222222","85466","BLR","1","10001",field,"60505661e0b9b354e134006d")
    return NewObjectID
"""
