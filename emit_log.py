import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

body = input('Insert body: ')

channel.basic_publish(exchange='logs', routing_key='', body=body)

print('[X] Sent')

connection.close()
