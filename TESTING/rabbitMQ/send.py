import pika

# Specify the IP you want to connect to here
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Create a recipient queue
channel.queue_declare(queue='hello')

# Specify queue name in 'routing_key' and message in 'body'
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print(" [x] Sent 'Hello World!'")

connection.close()
