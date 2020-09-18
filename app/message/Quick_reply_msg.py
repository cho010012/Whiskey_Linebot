from app import handler,line_bot_api
from linebot.models import *
import re
# 建立QuickReplyButton 提供使用者點選標籤
textQuickReplyButton1 = QuickReplyButton(action=MessageAction(label="鹹味",text="風味：鹹味"),image_url='')
textQuickReplyButton2 = QuickReplyButton(action=MessageAction(label="泥味",text="風味：泥土味"))
textQuickReplyButton3 = QuickReplyButton(action=MessageAction(label="花香",text="風味：花香味"))
textQuickReplyButton4 = QuickReplyButton(action=MessageAction(label="泥煤",text="風味：泥煤味"))
textQuickReplyButton5 = QuickReplyButton(action=MessageAction(label="辛香",text="風味：辛香香氣"))
textQuickReplyButton6 = QuickReplyButton(action=MessageAction(label="果香",text="風味：果香味"))
textQuickReplyButton7 = QuickReplyButton(action=MessageAction(label="穀物",text="風味：穀物味"))
textQuickReplyButton8 = QuickReplyButton(action=MessageAction(label="木質香",text="風味：木質香"))
textQuickReplyButton9 = QuickReplyButton(action=MessageAction(label="辛辣香氣",text="風味：辛辣香氣"))
textQuickReplyButton10 = QuickReplyButton(action=MessageAction(label="礦物香",text="風味：礦物香"))



cocktail_button1 = QuickReplyButton(action=MessageAction(label="圓熟",text="風味：圓熟"))
cocktail_button2 = QuickReplyButton(action=MessageAction(label="經典",text="風味：經典"))
cocktail_button3 = QuickReplyButton(action=MessageAction(label="原創",text="風味：獨創"))
cocktail_button4 = QuickReplyButton(action=MessageAction(label="草藥",text="風味：草藥"))
cocktail_button5 = QuickReplyButton(action=MessageAction(label="甜",text="風味：甜"))
cocktail_button6 = QuickReplyButton(action=MessageAction(label="酸",text="風味：酸"))
cocktail_button7 = QuickReplyButton(action=MessageAction(label="苦甜",text="風味：苦甜"))
cocktail_button8 = QuickReplyButton(action=MessageAction(label="細緻",text="風味：細緻"))
cocktail_button9 = QuickReplyButton(action=MessageAction(label="和諧",text="風味：和諧"))
cocktail_button10 = QuickReplyButton(action=MessageAction(label="柑橘",text="風味：柑橘"))
cocktail_button11 = QuickReplyButton(action=MessageAction(label="果香",text="風味：水果香"))


quickReplyList = QuickReply(
    items = [textQuickReplyButton1,textQuickReplyButton2,textQuickReplyButton3,textQuickReplyButton4,textQuickReplyButton5,textQuickReplyButton6,textQuickReplyButton7,textQuickReplyButton8,textQuickReplyButton9,textQuickReplyButton10]
)
cocktailReplyList = QuickReply(
    items = [cocktail_button1,cocktail_button2,cocktail_button3,cocktail_button4,cocktail_button5,cocktail_button6,cocktail_button7,cocktail_button8,cocktail_button9,cocktail_button10,cocktail_button11]
)
quickReplyTextSendMessage = TextSendMessage(text='請點選您喜歡的威士忌風味', quick_reply=quickReplyList)
cocktailTextSendMessage = TextSendMessage(text='請點選您喜歡的調酒風味', quick_reply=cocktailReplyList)