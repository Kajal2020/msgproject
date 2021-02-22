import requests

import json

def send_msg(number,message):
    url = 'GET https://www.fast2sms.com/dev/bulk'

    params = {
        'authorization':'iv6Z391s54TMK8DGb0kRxNoHQlSVFzJeyWPpXafACnBUYctq7EW6T9PfrpjUBA0LkKOZMh8leRs3Sui5',
        'sender id': 'FSTSMS',
        'message': 'message',
        'language': 'english',
        'route': 'p',
        'numbers': 'number',
    }
    response = requests.get(url,params = params)
    dict = response.json()
    print(dict)

send_msg("7045465699", "mini project")
