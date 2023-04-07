from MongoDB.models import Quotes, Authors
import connect_bd


if __name__ == "__main__":
    while True:
        command = input("Input command >>>")
        if command == 'exit':
            break
        list_command = command.split(":")
        match list_command[0]:
            case 'exit':
                break
            case 'name':
                try:
                    id_name = Authors.objects(fullname=list_command[1])
                    for id_n in id_name:
                        print(id_n.id)
                        result = Quotes.objects(author=id_n)
                        for q in result:
                            print(q.id, q.tags, q.quote)
                except:
                    print("Not found!")
            case 'tag':
                try:
                    result = Quotes.objects(tags=list_command[1])
                    for q in result:
                        print(q.id, q.tags, q.quote)
                except:
                    print("Not found!")
            case 'tags':
                try:
                    list_tags = list_command[1].split(",")
                    result = Quotes.objects(tags__in=list_tags)
                    for q in result:
                        print(q.id, q.tags, q.quote)
                except:
                    print("Not found!")
