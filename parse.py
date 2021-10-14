from soup import get_html_text

def parse_html_text(html_text):
    soup = get_html_text(html_text)
    get_company_name(soup)
    #for each in soup.find_all("a"):
        #print(each.text)
    return

def get_company_name(soup):
    for each in soup.find_all("h4", class_="c-job_offer-recruiter__name"):
        print(each.find("a").text)