from kafka import KafkaConsumer
import time
import json

class consumer():
    #   初始設定    
    def __init__(self):
        #   連線Kafka consumer
        self.kaf = KafkaConsumer('spark_tag_output',bootstrap_servers=['35.201.219.64:9092'])

    def linker(self):
        for msg in self.kaf:
            with open('cocktail_tag.json','w' ,encoding='utf-8') as f:
                json.dump(eval(msg.value), f)
            # print(eval(msg.value))

if __name__ == "__main__":
    api = consumer()
    api.linker()