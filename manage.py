import json
import apiai
from flask import Flask
import twilio.twiml
from twilio.rest import TwilioRestClient

# Twilio account info
account_sid = "AC7be2fce7b6a98dc4de8d6e3ae35b46fa"
auth_token = "a5af087e9984bd9feac14f6382e0f191"
account_num = "+61488811362"
client = TwilioRestClient(account_sid, auth_token)

# api.ai account info
CLIENT_ACCESS_TOKEN = "bde8711eca1e43fd9a6169f33b7f2c64"
ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello api.ai (from Flask!)'

@app.route("/", methods=['GET', 'POST'])
def server():
    from flask import request
    # get SMS input via twilio
    resp = twilio.twiml.Response()

    # get SMS metadata
    msg_from = request.values.get("From", None)
    msg = request.values.get("Body", None)
    
    
    newstr = msg.split()
    if newstr[0]!='Search' or newstr[0]!='Find out about' or newstr[0]!='Tell me about' or newstr[0]!='search' or newstr[0]!='Weather' or newstr[0]!='Convert':
        # prepare API.ai request
        req = ai.text_request()
        req.lang = 'en'  # optional, default value equal 'en'
        req.query = msg

        # get response from API.ai
        api_response = req.getresponse()
        responsestr = api_response.read().decode('utf-8')
        response_obj = json.loads(responsestr)
        if 'result' in response_obj:
            response = response_obj["result"]["fulfillment"]["speech"]
            # send SMS response back via twilio
            client.messages.create(to=msg_from, from_= account_num, body=response)
            
    else if newstr[0]!='Search' or newstr[0]!='Find out about' or newstr[0]!='Tell me about' or newstr[0]!='search':
        response = s(' '.join(newstr[1:]))
        client.messages.create(to=msg_from, from_= account_num, body=response)
    else if newstr[0]!='Weather':
        response = w(newstr[1])
        client.messages.create(to=msg_from, from_= account_num, body=response)
    else if newstr[0]!='Convert':
        response = curr_converter(newstr[1],newstr[2],newstr[3])
        client.messages.create(to=msg_from, from_= account_num, body=str(response))
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
