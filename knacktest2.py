import json
import urllib2
import urllib
  
# setup a filter
filters = urllib.quote_plus("[{\"field\":\"field_91\",\"operator\":\"is\",\"value\":\"Active\",\"field_name\":\"Expired Status\"}]")
  
# setup headers including API credentials
app_id = '568b7d4aa49d90dc15b4e80d'
headers = {
    "Content-Type": "application/json",
    "X-Knack-Application-Id": app_id,
    "X-Knack-REST-API-Key": 'knack'
}
  
# setup the API call URL
def get_usertoken(email, passwd):
    url = "https://api.knackhq.com/v1/applications/" + app_id + "/session"
    datas = '{ "email": "%s", "password": "%s" }' % (email, passwd)
    req = urllib2.Request(url, datas, headers)
    req.get_method = lambda: 'POST'
    f = None
      
    try:
        f = urllib2.urlopen(req)
    except urllib2.HTTPError, ex:
        if ex.fp:
            extra = ex.fp.read()
            print "Knack Error: %s" % extra
        else:
            raise
    data = json.loads(f.read())
    return data["session"]["user"]["token"]



admin_usertoken = get_usertoken('admin@test.com', 'test')
#teacher_usertoken = get_usertoken('teacher@test.com', 'test')

def get_recipes(level):
    headers['Authorization'] = admin_usertoken
    url = 'https://api.knackhq.com/v1/scenes/scene_105/views/view_200/records'
    filters = [
        {"field":"field_93",
         "operator":"is",
         "value":"568bdba7c1ad7dd8064314f2"}
        ]
 #   url += '?filters=' + json.dumps(filters)
    datas = None
    req = urllib2.Request(url, datas, headers)
    req.get_method = lambda: 'GET'
    f = None
      
    try:
        f = urllib2.urlopen(req)
    except urllib2.HTTPError, ex:
        if ex.fp:
            extra = ex.fp.read()
            print "Knack Error: %s" % extra
        else:
            raise
    if f:
        data = json.loads(f.read())
        return data
    return None


def get_classes():
    headers['Authorization'] = admin_usertoken
    url = 'https://api.knackhq.com/v1/scenes/scene_27/views/view_64/records'
    datas = None
    req = urllib2.Request(url, datas, headers)
    req.get_method = lambda: 'GET'
    f = None
      
    try:
        f = urllib2.urlopen(req)
    except urllib2.HTTPError, ex:
        if ex.fp:
            extra = ex.fp.read()
            print "Knack Error: %s" % extra
        else:
            raise
    if f:
        data = json.loads(f.read())
        return data
    return None

    
    
