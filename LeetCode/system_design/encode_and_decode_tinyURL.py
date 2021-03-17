import random, string
class Codec:
    def __init__(self):
        self.tinyUrls = {}
        self.longUrls = {}
        
    def encode(self, longUrl: str) -> str:
        tinyUrl = ''
        for _ in range(6):
            tinyUrl += random.choice(string.ascii_letters if random.randint(0, 1) else string.digits)
        self.tinyUrls[tinyUrl], self.longUrls[longUrl] = longUrl, tinyUrl
        return tinyUrl
        

    def decode(self, shortUrl: str) -> str:
        return self.tinyUrls[shortUrl]