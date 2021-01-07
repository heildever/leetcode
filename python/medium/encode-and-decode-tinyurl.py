# question can be found on leetcode.com/problems/encode-and-decode-tinyurl/

from random import choice
from string import ascii_letters, digits


class Codec:
    def __init__(self):
        self.lookup = dict()

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        key = "http://tinyurl.com/"
        key += "".join(choice(ascii_letters + digits) for x in range(5))
        self.lookup.update({key: longUrl})
        return key

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.lookup.get(shortUrl)


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
