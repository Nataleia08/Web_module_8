import pika
from MongoDB.models import Contact
from faker import Faker


fake = Faker("uk-UA")




def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='emails')

    for i in range(10):
        i_email = Contact(fullname=fake.name(), email=fake.email(), phone = fake.phone_number())
        i_email.save()
        channel.basic_publish(exchange='', routing_key='emails', body=json.dumps(i_email).encode())
    connection.close()


if __name__ == '__main__':
    main()