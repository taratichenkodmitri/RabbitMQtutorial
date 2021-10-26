#!/usr/bin/python3
import pika
import sys


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(
                'localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')

    message = ' '.join(sys.argv[1:]) or "Hello World!"
    channel.basic_publish(exchange='',
                        routing_key='hello',
                        body=message)

    connection.close()

if __name__ == "__main__":
    main()