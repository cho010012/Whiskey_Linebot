from kafka import KafkaProducer
import time

class Kafka_producer():
    #   連線Kafka    
    def __init__(self):
        self.client = KafkaProducer(bootstrap_servers=['35.201.219.64:9092'])
    #   傳送message
    def producer_send(self, topic, value):
        self.client.send(topic, value=value)
        self.client.flush()

def main_api(input_dict):
    k = Kafka_producer()
    k.producer_send('line_activity', bytes(str(input_dict), encoding='utf-8'))

