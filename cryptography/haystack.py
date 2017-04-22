import json
import base64

data = json.load(open('haystack.ce724d850027.json'))



for pair in data['haystack']:
    print bytes(base64.b64decode(pair['data']))
    #table[entry['data']] = entry['signature']

    
