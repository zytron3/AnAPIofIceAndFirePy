import requests
import Book

def get_books(number=None, name=None, fromReleaseDate=None, toReleaseDate=None):
    url = "https://www.anapioficeandfire.com/api/books/"
    if (number is not None):
        url += str(number) + "/"
    if name is None and fromReleaseDate is None and toReleaseDate is None:
        res = requests.get(url).json()
        if type(res) == dict:
            res = [res]
        return [Book.Book(*x.values()) for x in res]
    else:
        url += "?"
    if name is not None:
        url += "name=" + name + "&"
    if fromReleaseDate is not None:
        url += "fromReleaseDate=" + fromReleaseDate + "&"
    if toReleaseDate is not None:
        url += "toReleaseDate=" + toReleaseDate + "&"
    url = url[:-1]  
    
    res = requests.get(url).json()
    #only 1 book
    if (type(res) == dict):
        return [Book.Book(*res.values())]
    else:
        return [Book.Book(*(x.values())) for x in res]

print(get_books(number=2)[0].authors)
#print(get_books()[0].mediaType)