from app import line_bot_api, handler
from linebot.models import *
import json
# 告知handler收到unfollowevent時候
@handler.add(UnfollowEvent)
def handle_unfollow_event(event):
    # 取出消息內User的資料
    # get_profile 取得用戶個資
    user_profile = line_bot_api.get_profile(event.source.user_id)
    print(event)
    # 將用戶資訊存在檔案內
    # save file by python
    with open("./unfollow_user.txt", "a") as myfile:
        myfile.write(json.dumps(vars(user_profile),sort_keys=True))
        myfile.write('\r\n')