from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
import random
app = Flask(__name__)
#line_bot_api = LineBotApi('LINE_CHANNEL_ACCESS_TOKEN')
#line_handler = WebhookHandler('LINE_CHANNEL_SECRET')
line_bot_api = LineBotApi('BY19iyX62vjY44SUkgMnQdZy+1m2CcmaMRI1LuIAu9rGTnrA/bq+z09DhLauopG2/3QE7LiotSm4PpkIlagYRh98B1w3Xe8NJeUKqGj+sm8lgx0qP8rAr2zz7a/+L6GgM6/E0V8CyncE+jKQnXydMQdB04t89/1O/w1cDnyilFU=')
line_handler = WebhookHandler('d1521ed647402db942e57d66f3b758f8')

@app.route('/')
def home():
    return 'Hello World'

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


def myG():
    return random.randint(1,10)

@line_handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    getA=event.message.text        

    if getA =='0' :
        photopath='https://3d4b-125-231-106-243.ngrok-free.app'        
        imageURL = random.choice([photopath+'/static/a.jpg', photopath+'/static/b.jpg', photopath+'/static/c.jpg', photopath+'/static/d.jpg'])
        img_message = ImageSendMessage(original_content_url=imageURL, preview_image_url=imageURL)
        line_bot_api.reply_message(event.reply_token,img_message)
       
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="輸入0"))

if __name__ == "__main__":
    app.run()