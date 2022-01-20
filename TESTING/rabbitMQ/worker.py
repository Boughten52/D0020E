import os
import pika
import sys
import time


def main():
    # Specify the IP you want to connect to here
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Create a recipient queue (creating a queue with the same name in two different places still only produces
    # one queue). We can't be sure which file runs first, so we declare it wherever we need it
    channel.queue_declare(queue='task_queue', durable=True)

    print(" [*] Waiting for messages. To exit press CTRL+C")

    # Whenever we receive a message this function is called
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body.decode())
        time.sleep(body.count(b'.'))
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    # Tells RabbitMQ to not give more than one message to a worker at a time
    channel.basic_qos(prefetch_count=1)

    # Tell RabbitMQ that the above callback function should receive from the 'task_queue' queue
    channel.basic_consume(queue='task_queue', on_message_callback=callback)

    # Enters a loop that waits for messages and runs callback whenever necessary. Catch KeyboardInterrupt when shutdown
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
