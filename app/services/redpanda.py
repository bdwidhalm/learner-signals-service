import json
import random
from random import randint
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers = "localhost:9092",
    value_serializer=lambda m: json.dumps(m).encode('ascii')
)

topic = "learner-signals"

def on_success(metadata):
  print(f"Message produced to topic '{metadata.topic}' at offset {metadata.offset}")

def on_error(e):
  print(f"Error sending message: {e}")

def publish(msg):
  future = producer.send(topic, msg)
  future.add_callback(on_success)
  future.add_errback(on_error)
  producer.flush()
#   producer.close()

