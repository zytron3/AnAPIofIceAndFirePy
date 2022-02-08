import requests

class Book(object):
    def __init__(self, url, name, isbn, authors, numberOfPages, publisher, country, mediaType, released, characters, povCharacters):
        self.url = url
        self.name = name
        self.isbn = isbn
        self.authors = authors
        self.numberOfPages = numberOfPages
        self.publisher = publisher
        self.country = country
        self.mediaType = mediaType
        self.released = released
        #will be list of urls
        self.characters = characters
        self.characters_processed = None
        self.povCharacters = povCharacters
    
    @classmethod
    def fromurl(cls, url):
        json = requests.get(url).json()
        if (type(json) == dict):
            return [cls(*json.values())]
        else:
            return [cls(*(x.values())) for x in json]


