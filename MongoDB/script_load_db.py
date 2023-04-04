from models import Authors, Quotes
import connect

with open("author.json", "r") as fh:
    list_a = fh.read()
for a in list_a:
    na = Authors(fullname= a["fullname"], born_date = a["born_date"], born_location = a["born_location"], description = a["description"])
    na.save()

with open("quotes.json", "r") as fh:
    list_q = fh.read()
for q in list_q:
    nq = Quotes(tags = q["tags"], author = q["author"], quote = q["quote"])
    nq.save()
