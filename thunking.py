import json

def decode(data, default=lambda:{}):
    try:
        return json.loads(data)
    except ValueError:
        return default()

from datetime import *

def log(message, time=None):
    print('%s %s' % (message, time if time else str(datetime.now())))
    

    

    
