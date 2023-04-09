import pika
import sys
import connect_bd
from MongoDB.models import Contact


def callback(ch, method, properties, body):
    print(f" [x] Received {body}")
    Contact.objects(id=body.decode('utf-8')).update_one(send_sms=True)

def main():
    credentials = pika.PlainCredentials('guest', '0987654321')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='sms')

    channel.basic_consume(queue='sms', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')

    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)