from models import Authors, Quotes
import connect
import argparse

def find_quotes_tags(tag:str):


def find_qoutes_author_name(name:str):
    pass

def find_quotes_list_tags(tags):
    pass



def main():
    while True:
        command = input("Input command >>>")
        if command == 'exit':
            break
        list_command = command.split(":")
        match list_command[0]:
            case 'exit':
                break
            case 'name':
                result = Quotes.objects(author__fullname=list_command[1])
                print(result)
            case 'tag':
                result = Quotes.objects(tags=list_command[1])
                print(result)
            case 'tags':
                result = Quotes.objects(tags=list_command[1].split(","))
                print(result)



if __name__ == "__name__":
    main()
