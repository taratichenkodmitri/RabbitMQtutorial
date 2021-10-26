#!/usr/bin/python3
import pika
import time

def callback(ch, method, properties, body):
    print(" [x] Received %r" % (body,))
    ch.basic_ack(delivery_tag = method.delivery_tag)
    

def main():
	connection = pika.BlockingConnection(pika.ConnectionParameters(
               	'localhost'))
	channel = connection.channel()
	channel.queue_declare(queue='hello')

	channel.basic_consume(queue='hello',
						on_message_callback=callback)

	print(' [*] Waiting for messages. To exit press CTRL+C')
	channel.start_consuming()

if __name__ == "__main__":
    main()