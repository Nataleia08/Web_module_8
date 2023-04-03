


class validationError(Exeption):
    pass




def find_author(uuid):
    pass

def create_author():
    ...

def update_author():
    ...

def remove_author():
    ...

def find_qoutes():
    ...


def create_quotes():
    ...

def update_quotes():
    ...

def remove_quotes():
    ...

def main():
    try:
        match action:
            case 'create':
                new_author = create_author()
                print(new_author)
            case 'find':
                result = find_author()
                print(result)
            case 