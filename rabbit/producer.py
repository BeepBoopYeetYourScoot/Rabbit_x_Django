import sys

from pika import BlockingConnection, ConnectionParameters, BasicProperties


def send_log_message(message: str):
    # Присоединяемся к брокеру на локалхосте, открыв с ним соединение
    connection = BlockingConnection(ConnectionParameters('localhost'))

    # Открываем канал для передачи сообщений
    channel = connection.channel()
    channel.exchange_declare(exchange='logs', exchange_type='direct')

    # Объявляем очередь, в которую будут отправляться сообщения
    channel.queue_declare(queue='logs.message_queue', durable=True)

    # Отправляем сообщение в очередь
    # Note 1: Все сообщения должны проходить через обменники (exchanges)
    # Note 2: В данном примере отправка осуществляется через стандартный обменник,
    #         поэтому необходимо указать имя очереди (routing_key),
    #         в которую должно быть отправлено сообщение
    channel.basic_publish(exchange='logs',
                          routing_key='logs.message_queue',
                          body=message,
                          # delivery_mode=2 sets message as durable
                          properties=BasicProperties(delivery_mode=2))

    print('[x] Message sent!')

    # Закрываем соединение, чтобы удостовериться, что сетевые буферы были очищены
    # и что сообщение было доставлено в очередь
    connection.close()

