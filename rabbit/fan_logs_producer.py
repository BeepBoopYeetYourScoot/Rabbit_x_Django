import sys

from pika import BlockingConnection, ConnectionParameters, BasicProperties

connection = BlockingConnection(ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare('fan_logger', 'fanout')

# Пушим сообщения через временную очередь, которая отмирает после закрытия соединения с потребителем
result = channel.queue_declare('', exclusive=True)
channel.queue_bind(result.method.queue, 'fan_logger')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='fan_logger', routing_key='', body=message)
print(" [x] Sent %r" % message)
connection.close()
