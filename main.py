import requests
url = "https://www.anapioficeandfire.com/api/characters?page=1&pageSize=10"
print(url)

def get_books(number=None, name=None, fromReleaseDate=None, toReleaseDate=None):
    url = "https://www.anapioficeandfire.com/api/books/"
    if (number is not None):
        url += str(number) + "/"
    if name is None and fromReleaseDate is None and toReleaseDate is None:
        resp = requests.get(url)
        return resp
    else:
        url += "?"
    if name is not None:
        url += "name=" + name + "&"
    if fromReleaseDate is not None:
        url += "fromReleaseDate=" + fromReleaseDate + "&"
    if toReleaseDate is not None:
        url += "toReleaseDate=" + toReleaseDate + "&"
    url = url[:-1]  
    resp = requests.get(url)
    return resp

print(get_books(number=1).content)