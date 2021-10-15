import requests

class Communication:
    def get(self, url):
        return requests.get(url)
