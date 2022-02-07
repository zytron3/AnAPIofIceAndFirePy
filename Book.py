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
    """
    def get_characters(self):
        if self.characters_processed is not None:
            return self.characters_processed
        result = []
        for character in self.characters:
            result.append(get_character(character))
    """


