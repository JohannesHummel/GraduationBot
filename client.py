import requests
import json

def send_data(message):

    url = 'http://localhost:5005/webhooks/rest/webhook'
    myobj = {'sender': message.author.name, 'message': message.content}
    
    data = json.dumps(myobj)
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    x = requests.post(url, data = data, headers=headers).json()

    final_string = ''
    for e in x:
        final_string += e['text'] + "\n"
    return final_string