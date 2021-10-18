import sys, time

from pika import BlockingConnection, ConnectionParameters

severities = ['info', 'warning', 'error']


def main():
    connection = BlockingConnection(ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='direct_logs', exchange_type='direct')
    message_queue = channel.queue_declare('', exclusive=True)
    message_queue_name = message_queue.method.queue

    for severity in severities:
        channel.queue_bind(queue=message_queue_name, exchange='direct_logs', routing_key=severity)

    # Получение сообщений работает с помощью привязки callback-функции к очереди
    # При получении сообщения pika вызовет данную функцию

    def callback(ch, method, properties, body):
        print(f'[x] Received {body.decode()} on binding {method.routing_key}')
        time.sleep(body.count(b'.'))
        print('[V] Done!')
        # Подтверждаем получение и обработку сообщения
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)

    channel.basic_consume(queue=message_queue_name, on_message_callback=callback)

    print('[*] Waiting for messages. To exit: Press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)
