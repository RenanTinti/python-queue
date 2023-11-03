import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='orders', exchange_type='topic')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='orders', queue=queue_name, routing_key='orders')


def callback(ch, method, properties, body):
    print(f'Pedido recebido: {body}')


channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print('Aguardando recebimento de pedidos. Pressione Ctrl + C para sair')
channel.start_consuming()
