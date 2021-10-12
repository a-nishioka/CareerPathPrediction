from comm import get_http_request

def scrape_site(url):
    r = get_http_request(url)
    if(r.status_code == 200):
        print("Communication succeeded.\n")
    else:
        print("Communication failed.\n")
        return ""
    return r