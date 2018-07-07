from pprint import pprint
import requests

def weather(location):
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+location+'&APPID=9ab0a3813e743f262b06467de891d671')
    resp = 'Name: '+r['name']+'\n'+'Visibility: '+r['visibility']+'\n'+ 'Wind Speed: '+r['wind']['speed']+'\n'+'Description: '+r['description']
    return resp
    
