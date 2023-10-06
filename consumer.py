import time
from kafka import KafkaConsumer

consumer = KafkaConsumer('my_topic', bootstrap_servers='kafka-broker-1:9092, kafka-broker-2:9092, kafka-broker-3:9092', group_id='2000', enable_auto_commit=False)

def start_consumer():
    print("Consumer started.")
    for message in consumer:
        print(f"Received message: {message.value.decode('utf-8')}")

def stop_consumer():
    print("Consumer stopped.")
    consumer.close()


if __name__ == "__main__":
    while True:
        if consumer.poll(timeout_ms=600000) == {};
            print("No data. Stopping consumer.")
            stop_consumer()
        else:
            start_consumer()
