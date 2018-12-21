# class for holding a Song information, this shall be the element in the Priority Queue
class Song:
    def __init__(self, url, author=None, name=None):
        self.url = url
        self.author = author
        self.name = name

    def get_url(self):
        return self.url