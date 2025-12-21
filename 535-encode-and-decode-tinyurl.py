import hashlib


class Codec:
    BASE_URL = 'https://tinyurl.com'

    def __init__(self):
        self.code_to_url = {}
        self.url_to_code = {}

    def to_tiny_url(self, code: str) -> str:
        return f'{self.BASE_URL}/{code}'

    def encode(self, longUrl: str) -> str:
        '''
        Encodes a URL to a shortened URL
        '''
        if not longUrl:
            return self.to_tiny_url('')

        if longUrl in self.url_to_code:
            return self.to_tiny_url(self.url_to_code[longUrl])

        code = hashlib.md5(longUrl.encode()).hexdigest()[:6]
        collision_counter = 0
        while code in self.code_to_url and self.code_to_url[code] != longUrl:
            collision_counter += 1
            code = hashlib.md5(
                (longUrl + str(collision_counter)).encode()).hexdigest()[:6]
        self.code_to_url[code] = longUrl
        self.url_to_code[longUrl] = code
        return self.to_tiny_url(code)

    def decode(self, shortUrl: str) -> str:
        '''
        Decodes a shortened URL to its original URL
        '''
        code = shortUrl.split('/')[-1]
        if code not in self.code_to_url:
            return ''

        return self.code_to_url[code]


codec = Codec()
longUrl = 'https://google.com'
encodedUrl = codec.encode(longUrl)
print(f'longUrl: {longUrl}, encodedUrl: {encodedUrl}')
decodedUrl = codec.decode(encodedUrl)
print(f'decodedUrl: {decodedUrl}')
