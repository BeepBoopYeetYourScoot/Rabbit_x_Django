import sys

from pika import BlockingConnection, ConnectionParameters


def main():
    connection = BlockingConnection(ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare('hello')

    # Получение сообщений работает с помощью привязки callback-функции к очереди
    # При получении сообщения pika вызовет данную функцию

    def callback(ch, method, properties, body):
        print(f'[x] Received {body}')

    # Говорим, что при получении сообщения в очереди hello нужно вызывать callback-функцию
    # По идее, для того, чтобы ловить сообщения из данной очереди, мы должны точно знать,
    # что данная очередь существует на нашей стороне.
    # Нам это известно, потому что мы объявили очередь выше
    channel.basic_consume(queue='hello',
                          auto_ack=True,
                          on_message_callback=callback)

    print('[*] Waiting for messages. To exit: Press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)