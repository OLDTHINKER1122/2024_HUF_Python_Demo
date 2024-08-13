from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from urllib.request import urlopen
import ssl
import json
import os


app = Flask(__name__)
#line_bot_api = LineBotApi('LINE_CHANNEL_ACCESS_TOKEN')
#line_handler = WebhookHandler('LINE_CHANNEL_SECRET')
line_bot_api = LineBotApi('BY19iyX62vjY44SUkgMnQdZy+1m2CcmaMRI1LuIAu9rGTnrA/bq+z09DhLauopG2/3QE7LiotSm4PpkIlagYRh98B1w3Xe8NJeUKqGj+sm8lgx0qP8rAr2zz7a/+L6GgM6/E0V8CyncE+jKQnXydMQdB04t89/1O/w1cDnyilFU=')
line_handler = WebhookHandler('d1521ed647402db942e57d66f3b758f8')

url ='https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWA-FAAB3B91-B4D2-4C1F-9F3C-E2D01B4F718A&format=JSON'


ansA=[]
city=''

@app.route('/')
def home():
    return 'Hello World!'

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        line_handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


def myG(aa):
    ansA.clear()
    ssl._create_default_https_context = ssl._create_unverified_context
    response = urlopen(url)
    data = response.read()
    output = json.loads(data)
    location=output['records']['location']
    for i in location:
        city = i['locationName']
        if city==aa:
            wx = i['weatherElement'][0]['time'][0]['parameter']['parameterName']
            maxtT = i['weatherElement'][4]['time'][0]['parameter']['parameterName']
            mintT = i['weatherElement'][2]['time'][0]['parameter']['parameterName']
            ci = i['weatherElement'][3]['time'][0]['parameter']['parameterName']
            pop = i['weatherElement'][4]['time'][0]['parameter']['parameterName']
            
            ansA.append(city)
            ansA.append(wx)
            ansA.append(mintT)
            ansA.append(maxtT)
    return ansA



@line_handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if  event.message.text == "0":  
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="大香菇在搞笑"))

    elif event.message.text == "1":  
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=str(myG('臺中市'))))        

    elif event.message.text == "2":        
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=str(myG('臺北市'))))
        
    elif event.message.text=='3':            
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=str(myG('臺南市'))))
        
    elif event.message.text=='4':            
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=str(myG('新竹市'))))
        
    elif event.message.text=='5':
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=str(myG('桃園市'))))
        
    elif event.message.text=='6':            
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=str(myG('高雄市'))))
        
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="只有0-6的數字 否則大香菇會長出香菇"))

if __name__ == "__main__":
    app.run()