from pika import BlockingConnection, ConnectionParameters


def queue_send_hello():
    # Присоединяемся к брокеру на локалхосте, открыв с ним соединение
    connection = BlockingConnection(ConnectionParameters('localhost'))

    # Открываем канал для передачи сообщений
    channel = connection.channel()

    # Объявляем очередь, в которую будут отправляться сообщения
    channel.queue_declare(queue='hello')

    # Отправляем сообщение в очередь
    # Note 1: Все сообщения должны проходить через обменники (exchanges)
    # Note 2: В данном примере отправка осуществляется через стандартный обменник,
    #         поэтому необходимо указать имя очереди (routing_key),
    #         в которую должно быть отправлено сообщение
    channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')

    print('[x] Message sent!')

    # Закрываем соединение, чтобы удостовериться, что сетевые буферы были очищены
    # и что сообщение было доставлено в очередь
    connection.close()
