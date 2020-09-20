from app import line_bot_api, handler
from linebot.models import *
import json,re
from app.API.kafka_producer_line import main_api
# from app.API.cocktail_producer import cocktail_api
from app.API.luis_test import luis
from app.API.Redis_whiskey_tag import tag_api
from app.API.Redis_whiskey_name import name_api
from app.nlp.olami import Olami
import configparser
from app.message.Quick_reply_msg import quickReplyTextSendMessage, cocktailTextSendMessage
import calendar
import time



# 讀取 olami 憑證 secret連接api
config = configparser.ConfigParser()
config.read("../app/config.ini")
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    profile = line_bot_api.get_profile(event.source.user_id) # 使用者資訊
    msg = str(event.message.text).upper().strip()  # 使用者輸入的內容
    utterance = luis(msg) # Luis 自然語言處理語句
    uid = profile.user_id  # 發訊者ID
    Timestamp = calendar.timegm(time.gmtime())
    Name = profile.display_name
    Pic = profile.picture_url
    dict = {"Name": Name, "Picture": Pic, "UserID": uid, "Msg": msg, 'Timestamp': Timestamp}
    main_api(dict)
    if re.match('威士忌推薦', msg):
        line_bot_api.push_message(
            uid, quickReplyTextSendMessage)
    elif re.match('調酒推薦', msg):
        line_bot_api.push_message(
            uid, cocktailTextSendMessage)
# 文字觸發 推播 Liff 嵌入式網頁   #未來展望：取得jquery +評論+liff.profile資訊+更多功能
    elif re.match('酒吧地圖',msg):
        buttons_template = ButtonsTemplate(
            title='親愛的使用者', text='請點選下表連結到酒吧',
            actions=[uid,URIAction(label="將為您提供酒吧地圖",uri="https://liff.line.me/1654667223-V7pklmP5")])
        template_message = TemplateSendMessage(
            alt_text='將為您提供酒吧地圖', template=buttons_template)
        line_bot_api.reply_message(event.reply_token, template_message)
    elif re.match('尋找酒友',msg):
        buttons_template = ButtonsTemplate(
            title='親愛的使用者', text='請點選下表連結到聊天室',
            actions=[uid,URIAction(label="將為您提供酒友聊天室",uri="https://liff.line.me/1654667223-3aR1lyPv")])
        template_message = TemplateSendMessage(
            alt_text='將為您提供酒友聊天室', template=buttons_template)
        line_bot_api.reply_message(event.reply_token, template_message)

# 針對調酒風味re.match 文字訊息 作出reply

    elif re.match('關鍵字查詢', msg):
        line_bot_api.push_message(uid, TextSendMessage("請再輸入任意風味或酒名關鍵字"))
    elif re.match('熱門排行', msg):
        line_bot_api.push_message(uid, TextSendMessage("將為您提供熱門排行前五名"))
        Pop_message = json.load(open("./app/Json_message/popular", 'r', encoding="utf-8"))
        Pop_demo = FlexSendMessage.new_from_json_dict(Pop_message)
        line_bot_api.push_message(uid, Pop_demo)
    elif re.match('好酒貪杯', msg):
        IOT_message = json.load(open("./app/Json_message/Drink", 'r', encoding="utf-8"))
        IOT_demo = TemplateSendMessage.new_from_json_dict(IOT_message)
        line_bot_api.push_message(uid, IOT_demo)
    elif re.match('倒酒動作', msg):
        line_bot_api.push_message(uid, TextSendMessage("正在進行倒酒動作"))
    elif re.match('取消動作', msg):
        line_bot_api.push_message(uid, TextSendMessage("已為您取消動作"))
    elif re.match('資策會_EB102_愛心組', msg):
        line_bot_api.push_message(uid, TextSendMessage("https://ibar3.webnode.tw/"))
# 先透過關鍵字名稱找尋有無相關data 若無再利用標籤查詢data 再沒有則利用olami查詢是否有相關AI數據庫資訊
    else:
        try:
            data = name_api(msg)
            flexSendMessage1 = FlexSendMessage.new_from_json_dict(data)
            line_bot_api.push_message(uid, TextSendMessage("請稍等…將為您進行搜尋"))
            line_bot_api.push_message(uid, flexSendMessage1)
        except IndexError:
            data2 = tag_api(utterance)
            if not len(data2['contents']['contents'])==0:
                flexSendMessage2 = FlexSendMessage.new_from_json_dict(data2)
                line_bot_api.push_message(uid, TextSendMessage("請稍等…將為您進行搜尋"))
                line_bot_api.push_message(uid, flexSendMessage2)
            else:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=Olami().nli(event.message.text)))