from app import line_bot_api, handler,secretFileContentJson
from linebot.models import *
import json
'''

撰寫用戶關注時，我們要處理的商業邏輯

1. 取得用戶個資，並存回伺服器
2. 把先前製作好的自定義菜單，與用戶做綁定
3. 回應用戶，歡迎用的文字消息與圖片消息

'''
# 載入Follow事件
# 載入requests套件
# 告知handler，如果收到FollowEvent，則做下面的方法處理
@handler.add(FollowEvent)
def reply_text_and_get_user_profile(event):
    # 取出消息內User的資料
    profile = line_bot_api.get_profile(event.source.user_id)
    # 將用戶資訊存在檔案內
    with open("./users.txt", "a") as myfile:
        myfile.write(json.dumps(vars(profile), sort_keys=True))
        myfile.write('\r\n')
    # 將菜單綁定在用戶身上
    linkRichMenuId = secretFileContentJson.get("rich_menu_id")
    linkResult = line_bot_api.link_rich_menu_to_user(event.source.user_id, linkRichMenuId)
    # 對新關注用戶傳送文字訊息
    Follow1_message = json.load(open("../Json_message/Follow1", 'r', encoding="utf-8"))
    Follow2_message = json.load(open("../Json_message/Follow2", 'r', encoding="utf-8"))
    Follow1_demo = TextSendMessage.new_from_json_dict(Follow1_message)
    Follow2_demo = TextSendMessage.new_from_json_dict(Follow2_message)
    line_bot_api.push_message(event.source.user_id, Follow1_demo)
    line_bot_api.push_message(event.source.user_id, Follow2_demo)
