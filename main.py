import requests
from Book import Book
from Character import Character

def get_json(**params):
    url = "https://www.anapioficeandfire.com/api/" + params["type"] + "/"
    if params["id"] is not None:
        url += str(params["id"])
    url += "/?"
    del params["type"]
    del params["id"]
    for param in params.items():
        url += str(param[0]) + "=" + str(param[1]) + "&"
    url = url[:-1]
    return requests.get(url).json()

def get_books(id=None, name=None, fromReleaseDate=None, toReleaseDate=None):
    args = {key: value for (key, value) in locals().items() if value is not None}
    args["type"] = "books"
    json = get_json(**args)
    if (type(json) == dict):
        return [Book(*json.values())]
    else:
        return [Book(*(x.values())) for x in json]

def get_characters(id=None, name=None, gender=None, culture=None, born=None, died=None, isAlive=None):
    args = {key: value for (key, value) in locals().items() if value is not None}
    args["type"] = "characters"
    json = get_json(**args)
    if (type(json) == dict):
        return [Character(*json.values())]
    else:
        return [Character(*(x.values())) for x in json]

print(get_characters(id=2)[0].name)
#print(get_books()[0].mediaType)