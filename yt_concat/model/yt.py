
class YT:
    def __init__(self, url):
        self.url = url
        self.captions = None
        self.id = url.split('watch?v=')[-1]

    def __str__(self):
        return '<YT(' + self.id + ')>'

