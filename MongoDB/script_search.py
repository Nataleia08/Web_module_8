import redis

from MongoDB.models import Quotes, Authors
import connect_bd
from redis_lru import RedisLRU

client = redis.StrictRedis(host='localhost', port=6379, password=None)
cache = RedisLRU(client)


def name_command(text_command):
    try:
        id_name = Authors.objects(fullname=text_command)
        for id_n in id_name:
            result = Quotes.objects(author=id_n)
            return result

    except:
        print("Not found!")

def tag_command(text_command):
    try:
        result = Quotes.objects(tags=text_command)
        return result

    except:
        print("Not found!")


def tags_command(text_command):
    try:
        list_tags = text_command.split(",")
        result = Quotes.objects(tags__in=list_tags)
        return result
    except:
        print("Not found!")

def main():
    while True:
        command = input("Input command >>>")
        if command == 'exit':
            break
        list_command = command.split(":")
        for key in client.scan_iter():
            if command.startswith(key.decode()):
                cache.get(key)
                print("This is result in cache!")
                continue
        match list_command[0]:
            case 'exit': break
            case 'name':
                result = name_command(list_command[1])
                cache.set(command, result)
                for q in result:
                    print(str(q.id).encode(encoding='UTF-8'), str(q.tags).encode(encoding='UTF-8'),
                          str(q.quote).encode(encoding='UTF-8'))
            case 'tag':
                result = tag_command(list_command[1])
                cache.set(command, result)
                for q in result:
                    print(str(q.id).encode(encoding='UTF-8'), str(q.tags).encode(encoding='UTF-8'),
                          str(q.quote).encode(encoding='UTF-8'))
            case 'tags':
                result = tags_command(list_command[1])
                cache.set(command, result)
                for q in result:
                    print(str(q.id).encode(encoding='UTF-8'), str(q.tags).encode(encoding='UTF-8'),
                          str(q.quote).encode(encoding='UTF-8'))



if __name__ == "__main__":
    main()

