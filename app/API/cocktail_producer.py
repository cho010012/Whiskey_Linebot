from kafka import KafkaProducer
import time

class Kafka_producer():
    #   連線Kafka    
    def __init__(self):
        self.client = KafkaProducer(bootstrap_servers=['35.201.219.64:9092'])

    #   傳送message
    def producer_send(self, topic, value):
        self.client.send(topic, value=value)
        return self.client.close()

def cocktail_api(input_):
    k = Kafka_producer()
    k.producer_send('spark_tag_output', bytes(str(input_), encoding='utf-8'))

