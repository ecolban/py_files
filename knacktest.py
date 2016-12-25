import json
import urllib2
import urllib
  
# setup a filter
filters = urllib.quote_plus("[{\"field\":\"field_91\",\"operator\":\"is\",\"value\":\"Active\",\"field_name\":\"Expired Status\"}]")
  
# setup headers including API credentials
headers = {
    "Content-Type": "application/json",
    "X-Knack-Application-Id": '568b7d4aa49d90dc15b4e80d',
    "X-Knack-REST-API-Key": '9c7fed80-b385-11e5-b415-d5831081a8e8'
}
  
# setup the API call URL
#url = "https://api.knackhq.com/v1/objects/object_14/records?filters="+filters

#url = "https://api.knackhq.com/v1/objects"
url = "https://api.knackhq.com/v1/objects/object_16/records"
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
data = json.loads(f.read())

data.get('objects')
  
print json.dumps(data, indent=4, sort_keys=True)


