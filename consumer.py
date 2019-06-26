import pika
import time
from random import randint

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='test')
start_time = time.time()


def callback(ch, method, properties, body):
    time.sleep(randint(0, 9))
    print(f'[X] received {body} I sleep for:  {time.time()-start_time}')
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='test', on_message_callback=callback)

print('Waiting for a message...')
channel.start_consuming()
