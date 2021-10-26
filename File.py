
class File:
    path = "sample.html"

    def write_html(self, text): 
        f = open(self.path, 'w', encoding='UTF-8')
        f.writelines(text)
        f.close()