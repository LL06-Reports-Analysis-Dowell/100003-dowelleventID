def dowelllogin(username, password,  Base64 value of image, voice, face-accuracy, voice-accuracy, dowellclock, laguage, sessionID,location, device, OSver, conn, processID):
    loc=location
    con=con
    dev=device
    OS=OSver
    pid=processID
    user=username
    passwd=password
    field={"username":user,"passwd":passwd}
    login=dowellconnection(cluster,platform,database,collection,document,team_member_ID,function_ID,FETCH,field,update_field)
    try:
        dicto=json.loads(conn)
        if dicto["username"]:
            usr=dicto["username"]
        else:
            return "http://127.0.0.1:8000/accounts/register/"
    except:
        return "something wrong"
def register(username,password,email,first_name,last_name,role,contrycode,phone):
