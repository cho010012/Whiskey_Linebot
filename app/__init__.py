
"""

啟用伺服器基本樣板

"""

# 引用Web Server套件
from flask import Flask, request, abort

# 從linebot 套件包裡引用 LineBotApi 與 WebhookHandler 類別
from linebot import (
    LineBotApi, WebhookHandler
)

# 引用無效簽章錯誤
from linebot.exceptions import (
    InvalidSignatureError
)

# 載入json處理套件
import json
# import configparser

# 載入基礎設定檔
secretFileContentJson=json.load(open("./app/Key/line_secret_key",'r',encoding="utf-8"))
# print(secretFileContentJson)
server_url=secretFileContentJson.get("server_url")
linkRichMenuId = secretFileContentJson.get("rich_menu_id")
# 生成實體物件
line_bot_api = LineBotApi(secretFileContentJson.get("channel_access_token"))
handler = WebhookHandler(secretFileContentJson.get("secret_key"))

# 設定Server啟用細節
app = Flask(__name__)
# # 讀取 olami 憑證 secret連接api
# config = configparser.ConfigParser()
# config.read("config.ini")

# 提供clock.py回傳爬網資訊
@app.route("/", methods=['GET',"POST"])
def wake():
    return "wake up"


# 啟動server對外接口，使Line能丟消息進來
@app.route("/callback", methods=['POST'])
def callback():

    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    # print(body)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


from app.message import (
    Follow_event_msg,Image_event_msg,Quick_reply_msg,Reply_msg,Sticker_msg,Unfollow_event_msg
)

