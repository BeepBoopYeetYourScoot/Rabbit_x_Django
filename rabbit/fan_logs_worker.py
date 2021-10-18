from pika import BlockingConnection, ConnectionParameters

connection = BlockingConnection(ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare('fan_logger', 'fanout')

result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(queue_name, 'fan_logger')

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r" % body)
    channel.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(queue=queue_name, on_message_callback=callback)

channel.start_consuming()