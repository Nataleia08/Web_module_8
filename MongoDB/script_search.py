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
                result = Quotes.objects(author__in=list_command[1])
                print(result)
            case 'tag':
                result = Quotes.objects(tags=list_command[1])
                for q in result:
                    print(q.id, q.tags, (q.quote))
            case 'tags':
                list_tags = list_command[1].split(",")
                result = Quotes.objects(tags__in=list_tags)
                for q in result:
                    print(q.id, q.tags, q.quote)
