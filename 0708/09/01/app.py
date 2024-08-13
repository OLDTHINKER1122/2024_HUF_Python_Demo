from flask import Flask, request, abort,render_template
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)


channel_secret = 'd1521ed647402db942e57d66f3b758f8'
channel_access_token = 'BY19iyX62vjY44SUkgMnQdZy+1m2CcmaMRI1LuIAu9rGTnrA/bq+z09DhLauopG2/3QE7LiotSm4PpkIlagYRh98B1w3Xe8NJeUKqGj+sm8lgx0qP8rAr2zz7a/+L6GgM6/E0V8CyncE+jKQnXydMQdB04t89/1O/w1cDnyilFU='
LIFF_ID = '2005793395-XM3PvJye'
LIFF_URL = 'https://liff.line.me/2005793395-XM3PvJye'


line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK' 


@app.route('/liff')
def liff():
    return render_template('index.html', liffid = LIFF_ID)

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    input_text = event.message.text
    if input_text == '123':
        message = TemplateSendMessage(
                alt_text='按鈕樣板',
                template=ButtonsTemplate(
                    thumbnail_image_url='https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png', 
                    title='測試line liff',
                    text='請選擇：',
                    actions=[
                        URITemplateAction(
                            label='連結網頁',
                            uri=LIFF_URL,
                        ),
                    ]
                )
            )
        
        try:
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=input_text))

if __name__ == '__main__':
    app.run()