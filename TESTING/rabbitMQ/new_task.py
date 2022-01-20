import pika
import sys

# Specify the IP you want to connect to here
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Create a recipient queue
channel.queue_declare(queue='task_queue', durable=True)

# Create message
message = ' '.join(sys.argv[1:]) or "No message specified"

# Specify queue name in 'routing_key' and message in 'body'
channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
                      ))

print(" [x] Sent %r" % message)

connection.close()
