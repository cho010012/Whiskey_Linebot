from app import line_bot_api, handler
from linebot.models import *
@handler.add(MessageEvent,message=ImageMessage)
def handle_image_message(event):
#     請line_bot_api把圖片從line抓回來，儲存到本地端
#     圖片名字以消息的id做命名
#      line_bot_api get message content line-bot-sdk
    message_content = line_bot_api.get_message_content(event.message.id)
    file_name = event.message.id + '.jpg'
    # file_message = event.message.id + '.txt'
    with open(file_name, 'wb') as fd:
        for chunk in message_content.iter_content():
            fd.write(chunk)
#  請line_bot_api回復用戶，說圖片已儲存 最多五則回覆
#  line_bot_api reply TextSendMessage
    line_bot_api.reply_message(
        event.reply_token,
        [
        TextSendMessage(text="圖片已儲存，檔名為   " + file_name),
        TextSendMessage(text="感謝您提供圖片資訊。")
        ]
    )