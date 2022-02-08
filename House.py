import requests

class House(object):
    def __init__(self, url, name, region, coatOfArms, words, titles, seats, \
        currentLord, heir, overlord, founded, founder, diedOut, ancestralWeapons, cadetBranches, swornMembers):
        self.url = url
        self.name = name
        self.region = region
        self.coatOfArms = coatOfArms
        self.words = words
        self.titles = titles
        self.seats = seats
        self.currentLord = currentLord
        self.heir = heir
        self.overlord = overlord
        self.found = founded
        self.founder = founder
        self.diedOut = diedOut
        self.ancestralWeapons = ancestralWeapons
        self.cadetBranches = cadetBranches
        self.swornMembers = swornMembers

    @classmethod
    def fromurl(cls, url):
        json = requests.get(url).json()
        if (type(json) == dict):
            return [cls(*json.values())]
        else:
            return [cls(*(x.values())) for x in json]