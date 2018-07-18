"""
    description:

    TinyURL is a URL shortening service where you enter a URL such as 
    https://leetcode.com/problems/design-tinyurl and it returns a short URL such
    as http://tinyurl.com/4e9iAk.

    Design the encode and decode methods for the TinyURL service. There is no
    restriction on how your encode/decode algorithm should work. You just need to
    ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded
    to the original URL.

    Idea:

    The algorithm behind tinyurl algorithm have been talked in
    [stackoverflow](https://stackoverflow.com/questions/742013/how-to-code-a-url-shortener)

    The solution here is python implementaion of that algorithm.
"""
import math 

class Codec:
    def __init__(self):
        self.__database = {}
        self.__lookup= {}
        self.__id = 0
        self.__base = 62
        self.__digit_offset = 48
        self.__lowercase_offset = 61
        self.__uppercase_offset = 55

    def true_ord(self, char):
        """
        Turns a digit [char] in character representation
        from the number system with base [BASE] into an integer.
        """
        
        if char.isdigit():
            return ord(char) - self.__digit_offset
        elif 'A' <= char <= 'Z':
            return ord(char) - self.__uppercase_offset
        elif 'a' <= char <= 'z':
            return ord(char) - self.__lowercase_offset
        else:
            raise ValueError("%s is not a valid character" % char)

    def true_chr(self, integer):
        """
        Turns an integer [integer] into digit in base [BASE]
        as a character representation.
        """
        if integer < 10:
            return chr(integer + self.__digit_offset)
        elif 10 <= integer <= 35:
            return chr(integer + self.__uppercase_offset)
        elif 36 <= integer < 62:
            return chr(integer + self.__lowercase_offset)
        else:
            raise ValueError("%d is not a valid integer in the range of base %d" % (integer, self.__base))
 
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        # check longUrl is already in our database
        key = 0
        if longUrl in self.__lookup:
            key = self.__lookup[longUrl]
            return self.__database[key] 
        else:
            key = self.__id
            self.__lookup[longUrl] = key

            # get shortUrl from id where longUrl store
            shortUrl = ""
            if key == 0:
                shortUrl = "0"
            else:
                while key > 0:
                    remainder = key % self.__base
                    shortUrl = self.true_chr(remainder) + shortUrl
                    key //= self.__base
            self.__database[self.__id] = shortUrl
            self.__id += 1
            return shortUrl
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        # get id from shortUrl
        key = 0
        reversed_url = shortUrl[::-1]
        for idx, char in enumerate(reversed_url):
            key += self.true_ord(char) * int(math.pow(self.__base, idx))
        print(key)
        print(self.__database)
        if key in self.__database:
            for i, u in self.__lookup.items():
                if u == key:
                    return i
        else:
            raise ValueError("%s is not a valid shortUrl" % shortUrl)

if __name__ == "__main__":
    c = Codec()
    print(c.decode(c.encode("https://leetcode.com/problems/encode-and-decode-tinyurl/description/")))
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
