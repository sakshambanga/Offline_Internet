import json
from pprint import pprint
import requests
def curr_converter(from_, to_, amount):
#    resp = http://data.fixer.io/api/latest?access_key=db672faaade156014a84afcb3036bb35
    resp1 = requests.get('http://data.fixer.io/api/latest?access_key=db672faaade156014a84afcb3036bb35')
    resp = resp1.json()
    if resp["success"]:
        return ((amount/resp["rates"][from_])*resp["rates"][to_])
    return 0
    
