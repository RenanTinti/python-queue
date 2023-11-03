import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='direct')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

error_levels = ['ERR', 'WARN', 'DEBUG']
for error_level in error_levels:
    channel.queue_bind(exchange='logs', queue=queue_name, routing_key=error_level)


def callback(ch, method, properties, body):
    print(f'Mensagem log recebida: {body}')


channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print('Aguardando mensagens de log. Pressione Ctrl + C para sair')
channel.start_consuming()
