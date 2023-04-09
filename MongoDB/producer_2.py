import pika
from MongoDB.models import Contact
from faker import Faker
import json
import connect_bd


fake = Faker("uk-UA")


def main():
    credentials = pika.PlainCredentials('guest', '0987654321')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='emails')
    channel.queue_declare(queue='sms')

    for i in range(10):
        i_email = Contact(fullname=fake.name(), email=fake.email(), phone = fake.phone_number())
        i_email.save()
        messages = str(i_email.id)
        channel.basic_publish(exchange='', routing_key='emails', body=messages)

    for i in range(10):
        i_email = Contact(fullname=fake.name(), email=fake.email(), phone = fake.phone_number())
        i_email.save()
        messages = str(i_email.id)
        channel.basic_publish(exchange='', routing_key='sms', body=messages)
    connection.close()


if __name__ == '__main__':
    main()