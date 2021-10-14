from bs4 import BeautifulSoup


def get_html_text(html):
    return BeautifulSoup(html, 'html.parser')