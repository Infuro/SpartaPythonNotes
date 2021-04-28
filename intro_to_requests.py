import requests
import json
from pprint import pprint

#api outline here
#http://postcodes.io/

json_body = json.dumps({"postcodes":["PR3 OSG", "M456GN", "EX165BL", "HP226DB"]})
headers = {"Content-Type":"application/json"}

post_multi_req = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_body)

pprint(post_multi_req.json())
