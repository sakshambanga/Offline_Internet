import json
import response
def curr_converter(from_, to_, amount):
    resp = http://data.fixer.io/api/latest?access_key=db672faaade156014a84afcb3036bb35
    if resp["success"]:
        return ((amount/resp["rates"][from_])*resp["rates"][to_])
    return 0
    
