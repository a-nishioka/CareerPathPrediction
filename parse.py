from bs4 import BeautifulSoup

def parse_html_text(target):
    return BeautifulSoup(target, 'html.parser')