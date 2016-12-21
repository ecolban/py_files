from random import randrange, choice

class CookieJar(object):

    def __init__(self):
        self._is_open = False
        self._cookies = [choice(['Chocolate Chip Cookie', 'Macademia Nut Cookie', 'Raisin Cookie']) for _ in range(24)]

    def take(self):
        if self._is_open:
            return self._cookies.pop()
        else:
            raise ValueError("Cookie jar is closed")
        
    def open_jar(self):
        self._is_open = True

    def close(self):
        self._is_open = False

    def is_open(self):
        return self._is_open

    def __len__(self):
        return len(self._cookies)

    def __iter__(self):
        return self

    def next(self):
        if len(self) > 0:
            return self.take()
        else:
            raise StopIteration

class SelfClosing(object):

    def __init__(self, jar):
        self._jar = jar
        
    def __enter__(self):
        self._jar.open_jar()
        return self._jar

    def __exit__(self, *args):
        self._jar.close()

cookie_jar = CookieJar()

def take_cookie():
    with SelfClosing(cookie_jar) as jar:
	return jar.take()
