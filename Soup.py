from bs4 import BeautifulSoup


class Soup:
    def markup(self, html_text):
        return BeautifulSoup(html_text, 'html.parser')