import redis

from MongoDB.models import Quotes, Authors
import connect_bd
from redis_lru import RedisLRU

client = redis.StrictRedis(host='localhost', port=6339, password=1234567890, username=nata)
cache = RedisLRU(client)

@cache
def name_command(text_command):
    try:
        id_name = Authors.objects(fullname=text_command)
        for id_n in id_name:
            # print(id_n.id)
            result = Quotes.objects(author=id_n)
            for q in result:
                print(str(q.id).encode(encoding='UTF-8'), str(q.tags).encode(encoding='UTF-8'),
                      str(q.quote).encode(encoding='UTF-8'))
    except:
        print("Not found!")
@cache
def tag_command(text_command):
    try:
        result = Quotes.objects(tags=text_command)
        for q in result:
            print(str(q.id).encode(encoding='UTF-8'), str(q.tags).encode(encoding='UTF-8'),
                  str(q.quote).encode(encoding='UTF-8'))
    except:
        print("Not found!")
@cache
def tags_command(text_command):
    try:
        list_tags = text_command.split(",")
        result = Quotes.objects(tags__in=list_tags)
        for q in result:
            print(str(q.id).encode(encoding='UTF-8'), str(q.tags).encode(encoding='UTF-8'),
                  str(q.quote).encode(encoding='UTF-8'))
    except:
        print("Not found!")

def main():
    while True:
        command = input("Input command >>>")
        if command == 'exit':
            break
        list_command = command.split(":")
        match list_command[0]:
            case 'exit': break
            case 'name': name_command(list_command[1])
            case 'tag': tag_command(list_command[1])
            case 'tags': tags_command(list_command[1])


if __name__ == "__main__":
    main()

