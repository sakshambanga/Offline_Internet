from pprint import pprint
import json
import requests

def w(location):
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+location+'&APPID=9ab0a3813e743f262b06467de891d671')
    t = r.json()
    resp = 'Name: '+t['name']+'\n'+'Visibility: '+str(t['visibility'])+'\n'+ 'Wind Speed: '+str(t['wind']['speed'])+'\n'+'Description: '+t['weather'][0]['description']
    return str(resp)
    
