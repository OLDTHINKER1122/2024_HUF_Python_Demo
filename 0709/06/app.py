import requests

url = 'https://notify-api.line.me/api/notify'
token = 'XXXX'
headers = {
    'Authorization': 'Bearer ' + token 
}
data = {
    'message':'測試一下！'
}
data = requests.post(url, headers=headers, data=data)