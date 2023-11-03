import pika
import random
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='orders', exchange_type='topic')

channel.exchange_declare(exchange='logs', exchange_type='direct')

for _ in range(1000):
    message = 'PAZ'
    channel.basic_publish(exchange='orders', routing_key='orders', body=message)

    ttl = 300000
    error_levels = ['ERR', 'WARN', 'DEBUG']
    priority = {'ERR': 9, 'WARN': 1, 'DEBUG': 4}
    error_message = random.choice(error_levels)
    channel.basic_publish(
        exchange='logs',
        routing_key=error_message,
        body=f'{error_message} Message',
        properties=pika.BasicProperties(priority=priority[error_message], expiration=str(ttl)),
    )

    time.sleep(0.1)

print('Enviados 1000 ordens de compra e mensagens de erro')

connection.close()
