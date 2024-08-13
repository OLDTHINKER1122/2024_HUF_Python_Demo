#https://developers.line.biz/flex-simulator/
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import re
import os
app = Flask(__name__)

line_bot_api = LineBotApi('BY19iyX62vjY44SUkgMnQdZy+1m2CcmaMRI1LuIAu9rGTnrA/bq+z09DhLauopG2/3QE7LiotSm4PpkIlagYRh98B1w3Xe8NJeUKqGj+sm8lgx0qP8rAr2zz7a/+L6GgM6/E0V8CyncE+jKQnXydMQdB04t89/1O/w1cDnyilFU=')
line_handler = WebhookHandler('d1521ed647402db942e57d66f3b758f8')

@app.route('/')
def home():
    return 'Hello'

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



def Pre01():
    output_flex_message =FlexSendMessage(
    alt_text='hello',
    contents={
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://developers-resource.landpress.line.me/fx/clip/clip10.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Brown Cafe",
            "weight": "bold",
            "size": "sm",
            "wrap": True
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gray_star_28.png"
              },
              {
                "type": "text",
                "text": "4.0",
                "size": "xs",
                "color": "#8c8c8c",
                "margin": "md",
                "flex": 0
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "東京旅行",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "xs",
                    "flex": 5
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    },
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://developers-resource.landpress.line.me/fx/clip/clip11.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Brown&Cony's Restaurant",
            "weight": "bold",
            "size": "sm",
            "wrap": True
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gray_star_28.png"
              },
              {
                "type": "text",
                "text": "4.0",
                "size": "sm",
                "color": "#8c8c8c",
                "margin": "md",
                "flex": 0
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "東京旅行",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "xs",
                    "flex": 5
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    },
    {
      "type": "bubble",
      "size": "micro",
      "hero": {
        "type": "image",
        "url": "https://developers-resource.landpress.line.me/fx/clip/clip12.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "320:213"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Tata",
            "weight": "bold",
            "size": "sm"
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
              },
              {
                "type": "icon",
                "size": "xs",
                "url": "https://developers-resource.landpress.line.me/fx/img/review_gray_star_28.png"
              },
              {
                "type": "text",
                "text": "4.0",
                "size": "sm",
                "color": "#8c8c8c",
                "margin": "md",
                "flex": 0
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": "東京旅行",
                    "wrap": True,
                    "color": "#8c8c8c",
                    "size": "xs",
                    "flex": 5
                  }
                ]
              }
            ]
          }
        ],
        "spacing": "sm",
        "paddingAll": "13px"
      }
    }
  ]
}

 
)
    return output_flex_message

@line_handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    myT=event.message.text       
    if myT == "0":
        P01 = Pre01()        
        line_bot_api.reply_message(event.reply_token, P01 )           
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="輸入0"))

if __name__ == "__main__":
    app.run()