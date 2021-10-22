import sys

from pika import BlockingConnection, ConnectionParameters, BasicProperties


def send_log_message(message: str, topic: str):

    # Присоединяемся к брокеру на локалхосте, открыв с ним соединение
    connection = BlockingConnection(ConnectionParameters('localhost'))

    # Открываем канал для передачи сообщений
    channel = connection.channel()

    channel.exchange_declare(exchange='topic_logs', exchange_type='topic')
    result = channel.queue_declare(queue='', exclusive=True)
    channel.queue_bind(queue=result.method.queue, exchange='topic_logs', routing_key=topic)

    channel.basic_publish(exchange='topic_logs',
                          routing_key=topic,
                          body=message,
                          # delivery_mode=2 sets message as durable
                          properties=BasicProperties(delivery_mode=2))
    print('[x] Message sent!')

    # Закрываем соединение, чтобы удостовериться, что сетевые буферы были очищены
    # и что сообщение было доставлено в очередь
    connection.close()

