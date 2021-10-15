import Communication

class Crawler:

    def crawl(self, url):
        comm = Communication.Communication()
        r = comm.get(url)
        if(r.status_code == 200):
            print("Communication succeeded.\n")
            return r
        else:
            print("Communication failed. URL: " + url + "\n")
            return ""