from bs4 import BeautifulSoup


def get_html_text(html_text):
    return BeautifulSoup(html_text, 'html.parser')