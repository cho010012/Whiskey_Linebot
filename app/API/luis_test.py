########### Python 3.6 #############

#
# This quickstart shows how to predict the intent of an utterance by using the LUIS REST APIs.
#

import requests
def luis(x):
    try:

        ##########
        # Values to modify.

        # YOUR-APP-ID: The App ID GUID found on the www.luis.ai Application Settings page.
        appId = 'Luis AppID'

        # YOUR-PREDICTION-KEY: Your LUIS authoring key, 32 character value.
        prediction_key = 'Luis Key'

        # YOUR-PREDICTION-ENDPOINT: Replace with your authoring key endpoint.
        # For example, "https://westus.api.cognitive.microsoft.com/"
        prediction_endpoint = 'https://westus.api.cognitive.microsoft.com/'

        # 載入json處理套件
        # import json

        # 載入基礎設定檔
        # secretFileContentJson = json.load(open("./luis_secret_key", 'r', encoding="utf-8"))
        # appId = secretFileContentJson.get("appId")
        # prediction_key = secretFileContentJson.get("prediction_key")
        # prediction_endpoint = secretFileContentJson.get("prediction_endpoint")


        # The utterance you want to use.
        # utterance = input('請輸入語句')
        ##########

        # The headers to use in this REST call.
        headers = {
        }

        # The URL parameters to use in this REST call.
        params ={
            'query': x,
            'timezoneOffset': '0',
            'verbose': 'true',
            'show-all-intents': 'true',
            'spellCheck': 'false',
            'staging': 'false',
            'subscription-key': prediction_key
        }


        # Make the REST call.
        response = requests.get(f'{prediction_endpoint}luis/prediction/v3.0/apps/{appId}/slots/production/predict', headers=headers, params=params)
        ret=response.json()
        # Display the results on the console.
        # print(ret)
        # print('您輸入的是' + ret['query'])
        ret2=ret['prediction']
        final_ret=(ret2['topIntent'])
        return final_ret
        # for entity in ret['entities']:
        #     print(entity)
    except Exception as e:
        # Display the error string.
        print(f'{e}')
