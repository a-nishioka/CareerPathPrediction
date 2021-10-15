from bs4 import BeautifulSoup


class Soup:
    def get_html_text(self, html_text):
        return BeautifulSoup(html_text, 'html.parser')