import os
import pika
import sys


def main():
    # Specify the IP you want to connect to here
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Create a recipient queue (creating a queue with the same name in two different places still only produces
    # one queue). We can't be sure which file runs first, so we declare it wherever we need it
    channel.queue_declare(queue='hello')

    # Whenever we receive a message this function is called
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    # Tell RabbitMQ that the above callback function should receive from the 'hello' queue
    channel.basic_consume(queue='hello', auto_ack=True, on_message_callback=callback)

    # Enters a loop that waits for messages and runs callback whenever necessary. Catch KeyboardInterrupt when shutdown
    print(" [*] Waiting for messages. To exit press CTRL+C")
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
