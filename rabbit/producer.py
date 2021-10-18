import sys

from pika import BlockingConnection, ConnectionParameters, BasicProperties

severities = ['info', 'warning', 'error']


def send_log_message(message: str, severity='info'):
    if severity not in severities:
        raise AttributeError('Invalid log message type!')

    # Присоединяемся к брокеру на локалхосте, открыв с ним соединение
    connection = BlockingConnection(ConnectionParameters('localhost'))

    # Открываем канал для передачи сообщений
    channel = connection.channel()
    channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

    result = channel.queue_declare(queue='', exclusive=True)
    channel.queue_bind(queue=result.method.queue, exchange='direct_logs', routing_key=severity)
    # Отправляем сообщение в очередь
    # Note 1: Все сообщения должны проходить через обменники (exchanges)
    # Note 2: В данном примере отправка осуществляется через стандартный обменник,
    #         поэтому необходимо указать имя очереди (routing_key),
    #         в которую должно быть отправлено сообщение
    channel.basic_publish(exchange='direct_logs',
                          routing_key=severity,
                          body=message,
                          # delivery_mode=2 sets message as durable
                          properties=BasicProperties(delivery_mode=2))

    print('[x] Message sent!')

    # Закрываем соединение, чтобы удостовериться, что сетевые буферы были очищены
    # и что сообщение было доставлено в очередь
    connection.close()

