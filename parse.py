from soup import get_html_text
from so import get_back, get_forward

def parse_html_text(html_text):
    soup = get_html_text(html_text)
    get_offer_id(soup)
    get_company_name(soup)
    #for each in soup.find_all("a"):
        #print(each.text)
    return

def get_offer_id(soup):
    for each in soup.find_all("h4", class_="c-job_offer-recruiter__name"):
        href = each.find("a").get("href")
        back = get_back("=", href)
        id = get_forward("#", back)
        print(id)

def get_company_name(soup):
    for each in soup.find_all("h4", class_="c-job_offer-recruiter__name"):
        print(each.find("a").text)