from mongoengine import Document
from mongoengine.fields import ListField, StringField, DateField, ReferenceField


class Authors(Document):
    fullname = StringField()
    born_date = DateField()
    born_location = StringField()
    description = StringField()
class Quotes(Document):
    tags = ListField(StringField())
    author = ReferenceField(Authors)
    quote = StringField()
